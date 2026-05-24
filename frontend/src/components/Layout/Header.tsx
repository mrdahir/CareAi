import { Link, NavLink } from "react-router-dom";
import { Heart } from "lucide-react";
import { LANGUAGES } from "../../types/common";
import { useAppStore } from "../../store/useAppStore";
import { useT } from "../../i18n/useT";

export default function Header() {
  const { language, setLanguage } = useAppStore();
  const tr = useT();

  const nav = [
    { to: "/", label: tr("nav.home") },
    { to: "/chat", label: tr("nav.chat") },
    { to: "/recommend", label: tr("nav.recommend") },
    { to: "/myth-buster", label: tr("nav.myth") },
    { to: "/about", label: tr("nav.about") },
  ];

  return (
    <header className="border-b border-care-100 bg-white/90 backdrop-blur sticky top-0 z-50">
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-4 py-3">
        <Link to="/" className="flex items-center gap-2 font-semibold text-care-800">
          <Heart className="h-6 w-6 text-care-600" aria-hidden />
          CareApp
        </Link>
        <nav className="hidden sm:flex gap-1" aria-label="Main">
          {nav.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `rounded-lg px-3 py-1.5 text-sm ${
                  isActive ? "bg-care-100 text-care-800 font-medium" : "text-gray-600 hover:bg-care-50"
                }`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
        <select
          aria-label="Language"
          value={language}
          onChange={(e) => setLanguage(e.target.value as typeof language)}
          className="rounded-lg border border-care-200 bg-white px-2 py-1 text-sm"
        >
          {LANGUAGES.map((l) => (
            <option key={l.code} value={l.code}>
              {l.label}
            </option>
          ))}
        </select>
      </div>
      <nav className="flex sm:hidden overflow-x-auto gap-1 px-4 pb-2" aria-label="Mobile">
        {nav.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              `whitespace-nowrap rounded-lg px-3 py-1 text-xs ${
                isActive ? "bg-care-100 text-care-800" : "text-gray-600"
              }`
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </header>
  );
}
