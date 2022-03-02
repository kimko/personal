# import logging
from typing import Dict

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

from app.models.or_tools_solver import OrToolsSolverPayloadSchema

# TODO logger
# log = logging.getLogger("uvicorn")


async def solve_TSP(payload: OrToolsSolverPayloadSchema) -> Dict:
    data = parse_payload(payload)
    print("solve_TSP")
    manager, routing, solution = build_routing_model_and_solve(data)
    return format_response(data, manager, routing, solution)


def parse_payload(payload: OrToolsSolverPayloadSchema):
    duration_matrix = payload.duration_matrix
    data = {}
    data["distance_matrix"] = [
        [duration + (payload.minutes_at_site * 60) for duration in durations]
        for durations in duration_matrix
    ]
    data["num_vehicles"] = payload.num_vehicles
    data["depot"] = 0
    data["capacity"] = payload.capacity_hours * 60 * 60  # 8 hours capacity
    return data


def build_routing_model_and_solve(data):
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )
    routing = pywrapcp.RoutingModel(manager)

    # TODO: refactor callback
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    dimension_name = "Distance"
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        data["capacity"],
        True,  # start cumul to zero
        dimension_name,
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)
    # The method SetGlobalSpanCostCoefficient sets a large coefficient (100) for the global span
    # of the routes, which in this example is the maximum of the distances of the routes. This makes
    # the global span the predominant factor in the objective function, so the program minimizes the
    # length of the longest route.

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    return manager, routing, routing.SolveWithParameters(search_parameters)


def format_response(data, manager, routing, solution):
    solution_map = {}
    print(f"Objective: {solution.ObjectiveValue()}")
    max_route_distance = 0
    for vehicle_id in range(data["num_vehicles"]):
        current_route = [0]
        index = routing.Start(vehicle_id)
        plan_output = "Route for vehicle {}:\n".format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += " {} -> ".format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            current_distance = routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id
            )
            route_distance += current_distance
            current_route.append(manager.IndexToNode(index))

        plan_output += "{}\n".format(manager.IndexToNode(index))
        plan_output += "Duration of the route: {} hours\n".format(
            round(route_distance / 60 / 60)
        )
        print(plan_output)
        solution_map[vehicle_id] = {
            "stops": current_route,
            "duration_minutes": round(route_distance / 60),
        }
        max_route_distance = max(route_distance, max_route_distance)

    print(
        f"Maximum of the route distances: {round(max_route_distance / 60 / 60 )} hours"
    )
    return solution_map
