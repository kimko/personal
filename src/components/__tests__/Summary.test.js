import React from "react";
import { render, cleanup } from "@testing-library/react";

import { Summary } from "../cvSummary";

afterEach(cleanup);

const title = "title asdf";
const shortDescription = `description asdf`;
const summary = ["qwert", "yuiop", "asdf", "ghjkl", "zxcvb"];

it("renders a Summary", () => {
  const { getByTestId, asFragment } = render(
    <Summary
      title={title}
      shortDescription={shortDescription}
      summary={summary}
    />,
  );

  expect(getByTestId("test-article-summary")).toBeInTheDocument();
  expect(asFragment()).toMatchSnapshot();
});
