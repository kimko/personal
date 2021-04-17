import React from "react";
import { render, cleanup } from "@testing-library/react";

import { Nav } from "../nav";

afterEach(cleanup);

const name = "Angela Merkel";
const email = "kanzler@bundestag.de";
const phone = { raw: "+11234567890", pretty: "1-123-456-7890" };

it("renders a Nav section", () => {
  const { getByTestId, asFragment } = render(
    <Nav name={name} email={email} phone={phone} />,
  );

  expect(getByTestId("test-section-nav")).toBeInTheDocument();
  expect(asFragment()).toMatchSnapshot();
});
