import React from "react";
import { render, cleanup } from "@testing-library/react";

import { Cv } from "../cv";

afterEach(cleanup);

it("renders a Cv", () => {
  const { getByTestId } = render(<Cv />);

  expect(getByTestId("test-section-nav")).toBeInTheDocument();
  expect(getByTestId("test-article-summary")).toBeInTheDocument();
  expect(getByTestId("test-section-experience")).toBeInTheDocument();
  expect(getByTestId("test-section-skills")).toBeInTheDocument();
  expect(getByTestId("test-footer-social")).toBeInTheDocument();
});
