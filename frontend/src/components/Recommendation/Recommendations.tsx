import type { RecommendResponse } from "../../types/recommendation";
import RecommendationCard from "./RecommendationCard";

export default function Recommendations({ data }: { data: RecommendResponse }) {
  return (
    <div className="space-y-4">
      <h2 className="text-xl font-semibold text-care-800">Your recommendations</h2>
      {data.recommendations.map((item) => (
        <RecommendationCard key={item.method_id} item={item} />
      ))}
      <p className="text-xs text-gray-500">{data.disclaimer}</p>
    </div>
  );
}
