import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import Button from "./Button";

describe("Button", () => {
  it("renders label", () => {
    render(<Button>Send</Button>);
    expect(screen.getByRole("button", { name: "Send" })).toBeInTheDocument();
  });

  it("can be disabled", () => {
    render(<Button disabled>Send</Button>);
    expect(screen.getByRole("button")).toBeDisabled();
  });
});
