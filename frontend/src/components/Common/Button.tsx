import { ButtonHTMLAttributes } from "react";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "ghost";
}

export default function Button({
  variant = "primary",
  className = "",
  children,
  ...props
}: Props) {
  const base =
    "inline-flex items-center justify-center rounded-lg px-4 py-2 text-sm font-medium transition focus:outline-none focus:ring-2 focus:ring-care-500 disabled:opacity-50";
  const variants = {
    primary: "bg-care-600 text-white hover:bg-care-700",
    secondary: "bg-white border border-care-200 text-care-800 hover:bg-care-50",
    ghost: "text-care-700 hover:bg-care-100",
  };
  return (
    <button className={`${base} ${variants[variant]} ${className}`} {...props}>
      {children}
    </button>
  );
}
