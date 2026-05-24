import { Link } from "react-router-dom";
import Button from "../components/Common/Button";
import { useT } from "../i18n/useT";

export default function NotFound() {
  const tr = useT();
  return (
    <div className="text-center py-16">
      <h1 className="text-4xl font-bold text-care-800">404</h1>
      <p className="mt-2 text-gray-600">{tr("notFound")}</p>
      <Link to="/" className="inline-block mt-6">
        <Button>{tr("nav.home")}</Button>
      </Link>
    </div>
  );
}
