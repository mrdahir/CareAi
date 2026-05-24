import { useEffect, useState } from "react";
import Card from "./Card";
import Loading from "./Loading";
import { fetchProgrammeSummary, type ProgrammeSummary } from "../../services/programmeService";
import { useT } from "../../i18n/useT";

export default function ProgrammeStats() {
  const tr = useT();
  const [data, setData] = useState<ProgrammeSummary | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetchProgrammeSummary()
      .then(setData)
      .catch(() => setError(true));
  }, []);

  if (error) return null;
  if (!data) return <Loading />;

  return (
    <Card className="bg-care-50/50 border-care-200">
      <h2 className="text-sm font-semibold text-care-800">{tr("programme.title")}</h2>
      <p className="text-xs text-gray-600 mt-1">{data.programme}</p>
      <dl className="mt-3 grid grid-cols-2 gap-2 text-xs sm:grid-cols-4">
        <Stat label={tr("programme.visits")} value={data.total_client_visits.toLocaleString()} />
        <Stat label={tr("programme.counselled")} value={data.counselled_rate} />
        <Stat label={tr("programme.counties")} value={String(data.county_count)} />
        <Stat label={tr("programme.topMethod")} value={data.top_methods[0]?.method ?? "—"} />
      </dl>
      <ul className="mt-3 flex flex-wrap gap-2 text-xs">
        {data.top_methods.map((m) => (
          <li
            key={m.method}
            className="rounded-full bg-white px-2 py-0.5 border border-care-100 text-care-800"
          >
            {m.method} {m.share}
          </li>
        ))}
      </ul>
    </Card>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-gray-500">{label}</dt>
      <dd className="font-semibold text-care-900">{value}</dd>
    </div>
  );
}
