import { useState } from "react";
import Survey from "../components/Recommendation/Survey";
import Recommendations from "../components/Recommendation/Recommendations";
import Loading from "../components/Common/Loading";
import ErrorMessage from "../components/Common/ErrorMessage";
import { getRecommendations } from "../services/recommendService";
import { useT } from "../i18n/useT";
import type { RecommendRequest, RecommendResponse } from "../types/recommendation";

export default function RecommendPage() {
  const tr = useT();
  const [result, setResult] = useState<RecommendResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleComplete = async (data: RecommendRequest) => {
    setLoading(true);
    setError(null);
    try {
      const res = await getRecommendations(data);
      setResult(res);
    } catch (err) {
      setError(err instanceof Error ? err.message : tr("error.generic"));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-care-900">{tr("recommend.title")}</h1>
      {!result && !loading && <Survey onComplete={handleComplete} />}
      {loading && <Loading />}
      {error && <ErrorMessage message={error} />}
      {result && (
        <>
          <button
            type="button"
            className="text-sm text-care-600 hover:underline"
            onClick={() => setResult(null)}
          >
            {tr("recommend.back")}
          </button>
          <Recommendations data={result} />
        </>
      )}
    </div>
  );
}
