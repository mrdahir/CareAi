import type { RecommendationItem } from "../../types/recommendation";
import Card from "../Common/Card";

function scoreColor(score: number) {
  if (score >= 80) return "text-green-600 bg-green-50";
  if (score >= 60) return "text-amber-600 bg-amber-50";
  return "text-orange-600 bg-orange-50";
}

export default function RecommendationCard({ item }: { item: RecommendationItem }) {
  return (
    <Card>
      <div className="flex justify-between items-start gap-2">
        <div>
          <span className="text-xs text-gray-500">#{item.rank}</span>
          <h3 className="text-lg font-semibold text-care-800">{item.method}</h3>
        </div>
        <span
          className={`rounded-full px-2 py-1 text-xs font-bold ${scoreColor(item.match_score)}`}
        >
          {item.match_score}% match
        </span>
      </div>
      <dl className="mt-3 grid grid-cols-2 gap-2 text-sm">
        <div>
          <dt className="text-gray-500">Effectiveness</dt>
          <dd className="font-medium">{item.effectiveness}</dd>
        </div>
        <div>
          <dt className="text-gray-500">Duration</dt>
          <dd className="font-medium">{item.duration}</dd>
        </div>
        <div className="col-span-2">
          <dt className="text-gray-500">Side effects</dt>
          <dd>{item.side_effects}</dd>
        </div>
      </dl>
      <ul className="mt-3 list-disc pl-5 text-sm text-gray-700 space-y-1">
        {item.key_reasons.map((r) => (
          <li key={r}>{r}</li>
        ))}
      </ul>
      {item.regional_popularity && (
        <p className="mt-2 text-xs text-care-700">{item.regional_popularity}</p>
      )}
      <p className="mt-3 text-xs text-gray-500">{item.next_steps}</p>
    </Card>
  );
}
