import React from "react";
import { render, cleanup } from "@testing-library/react";

import { Experience } from "../cvExperience";

afterEach(cleanup);

const jobData = [
  {
    start: "2020",
    end: "Present",
    title: "Cat Herder",
    company: "Cats'r'Us",
    location: "Portland, OR",
    experience: [
      {
        task: `Play with Cats.`,
        tools: ["yarn", "flashlight"],
      },
      {
        task: `Fed the Cats`,
        tools: ["Milk", "Kibble"],
      },
    ],
  },
  {
    start: "2018",
    end: "2020",
    title: "Hahum",
    company: "Hmm",
    location: "Portland, OR",
    experience: [
      {
        task: `Task task task task task task.`,
        tools: ["tool1", "tool2", "tool3"],
      },
      {
        task: `asdf jkl;`,
        tools: ["a", "b", "d"],
      },
    ],
  },
];

it("renders a Experience section", () => {
  const { getByTestId, asFragment } = render(<Experience jobData={jobData} />);

  expect(getByTestId("test-section-experience")).toBeInTheDocument();
  expect(asFragment()).toMatchSnapshot();
});
