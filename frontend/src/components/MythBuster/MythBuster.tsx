import { useState } from "react";
import Card from "../Common/Card";
import Button from "../Common/Button";
import Loading from "../Common/Loading";
import ErrorMessage from "../Common/ErrorMessage";
import { checkMyth, type MythCheckResponse } from "../../services/mythService";
import { useAppStore } from "../../store/useAppStore";
import { useT } from "../../i18n/useT";

export default function MythBuster() {
  const { language } = useAppStore();
  const tr = useT();
  const [statement, setStatement] = useState("");
  const [result, setResult] = useState<MythCheckResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submit = async () => {
    if (!statement.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const data = await checkMyth(statement.trim(), language);
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : tr("error.generic"));
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="space-y-4">
      <h2 className="text-lg font-semibold text-care-800">{tr("myth.title")}</h2>
      <p className="text-sm text-gray-600">{tr("myth.intro")}</p>
      <textarea
        value={statement}
        onChange={(e) => setStatement(e.target.value)}
        rows={3}
        placeholder={tr("myth.placeholder")}
        className="w-full rounded-lg border border-care-200 px-3 py-2 text-sm"
        aria-label={tr("myth.intro")}
      />
      <Button onClick={submit} disabled={loading || !statement.trim()}>
        {tr("myth.submit")}
      </Button>
      {loading && <Loading />}
      {error && <ErrorMessage message={error} />}
      {result && (
        <div
          className={`rounded-lg p-4 text-sm ${
            result.is_myth
              ? "bg-amber-50 border border-amber-200"
              : "bg-care-50 border border-care-200"
          }`}
        >
          <p className="font-semibold">
            {result.is_myth ? tr("myth.isMyth") : tr("myth.factCheck")}
            {result.is_myth && (
              <span className="ml-2 text-xs uppercase text-amber-700">
                {tr("myth.severity")}: {result.severity}
              </span>
            )}
          </p>
          <p className="mt-2">
            <strong>{tr("myth.fact")}:</strong> {result.fact}
          </p>
          <p className="mt-2 text-gray-700">{result.evidence}</p>
          {result.sources.length > 0 && (
            <p className="mt-2 text-xs text-gray-500">
              {tr("myth.sources")}: {result.sources.join(", ")}
            </p>
          )}
        </div>
      )}
    </Card>
  );
}
