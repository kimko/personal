from faker import Faker

f = Faker()
f.random.seed(42)


def generate_experience(tools):
    return {"task": f.text(), "tools": f.words(tools)}


def generate_job(experience, tools):
    return {
        "start": f.date(),
        "end": f.date(),
        "title": f.job(),
        "company": f.company(),
        "location": f"{f.city()}, {f.state_abbr()}",
        "experience": [generate_experience(tools) for _ in range(0, experience + 1)],
    }


def generate_payload(jobs=2, experience=2, tools=4, skills=5):
    return {
        "title": f.job(),
        "short_description": f.text(),
        "name": f.name(),
        "email": f.email(),
        "phone": f.phone_number(),
        "public_id": f.text(6),
        "summary": f.words(5),
        "jobs": [generate_job(experience, tools) for _ in range(0, jobs)],
        "skills": {f.word(): f.words(f.random_digit() + 2) for _ in range(0, skills)},
    }


def generate_ots_payload():
    return {"capacity_hours": 8, "num_vehicles": 10, "minutes_at_site": 5}
