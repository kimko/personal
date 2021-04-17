import React from "react";
import { render, cleanup } from "@testing-library/react";

import { Skills } from "../cvSkills";

afterEach(cleanup);

const skillData = {
  animals: ["cats", "red-pandas"],
  other: ["skill", "data"],
};

it("renders a Skill section", () => {
  const { getByTestId, asFragment } = render(<Skills skillData={skillData} />);

  expect(getByTestId("test-section-skills")).toBeInTheDocument();
  expect(asFragment()).toMatchSnapshot();
});
