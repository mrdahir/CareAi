import { ReactNode } from "react";
import Header from "./Header";

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-6">{children}</main>
      <footer className="border-t border-care-100 bg-white py-4 text-center text-xs text-gray-500">
        CareApp provides general health education only — not medical advice. Consult a
        healthcare provider.
      </footer>
    </div>
  );
}
