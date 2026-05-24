import Card from "../components/Common/Card";
import { useT } from "../i18n/useT";

export default function About() {
  const tr = useT();
  return (
    <div className="space-y-4 max-w-2xl">
      <h1 className="text-2xl font-bold text-care-900">{tr("about.title")}</h1>
      <Card>
        <p className="text-sm text-gray-700 leading-relaxed">{tr("about.p1")}</p>
        <p className="mt-4 text-sm text-gray-700">{tr("about.p2")}</p>
      </Card>
    </div>
  );
}
