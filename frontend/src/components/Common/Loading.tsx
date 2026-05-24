export default function Loading({ label = "Loading..." }: { label?: string }) {
  return (
    <div className="flex items-center gap-2 text-care-700" role="status" aria-live="polite">
      <span className="h-4 w-4 animate-spin rounded-full border-2 border-care-600 border-t-transparent" />
      <span className="text-sm">{label}</span>
    </div>
  );
}
