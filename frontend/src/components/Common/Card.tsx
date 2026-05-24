import { ReactNode } from "react";

export default function Card({
  children,
  className = "",
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={`rounded-xl border border-care-100 bg-white p-4 shadow-sm ${className}`}
    >
      {children}
    </div>
  );
}
