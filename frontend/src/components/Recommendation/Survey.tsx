import { useState } from "react";
import Button from "../Common/Button";
import type { RecommendRequest } from "../../types/recommendation";
import { useAppStore } from "../../store/useAppStore";
import { useT } from "../../i18n/useT";

const STEPS = 6;

interface Props {
  onComplete: (data: RecommendRequest) => void;
}

export default function Survey({ onComplete }: Props) {
  const { language } = useAppStore();
  const tr = useT();
  const [step, setStep] = useState(0);
  const [form, setForm] = useState<RecommendRequest>({
    age: 25,
    breastfeeding: false,
    months_postpartum: 0,
    pregnancy_goals: "space_children",
    health_conditions: [],
    side_effect_tolerance: [],
    preferred_duration: "long_term",
    cost_sensitive: false,
    privacy_needed: false,
    region: "Kenya",
    language,
  });

  const next = () => {
    if (step < STEPS - 1) setStep(step + 1);
    else onComplete({ ...form, language });
  };
  const back = () => setStep(Math.max(0, step - 1));

  const progress = ((step + 1) / STEPS) * 100;

  return (
    <div className="space-y-4">
      <p className="text-sm text-gray-600">{tr("recommend.surveyTitle")}</p>
      <div className="h-2 rounded-full bg-care-100 overflow-hidden">
        <div
          className="h-full bg-care-600 transition-all"
          style={{ width: `${progress}%` }}
          role="progressbar"
          aria-valuenow={progress}
        />
      </div>

      {step === 0 && (
        <label className="block">
          <span className="text-sm font-medium">{tr("recommend.age")}</span>
          <input
            type="number"
            min={15}
            max={49}
            value={form.age}
            onChange={(e) => setForm({ ...form, age: Number(e.target.value) })}
            className="mt-1 w-full rounded-lg border border-care-200 px-3 py-2"
          />
        </label>
      )}
      {step === 1 && (
        <fieldset>
          <legend className="text-sm font-medium">{tr("recommend.goals")}</legend>
          {(
            [
              ["space_children", tr("recommend.goals.space")],
              ["prevent_pregnancy", tr("recommend.goals.prevent")],
              ["flexible", tr("recommend.goals.flexible")],
            ] as const
          ).map(([val, label]) => (
            <label key={val} className="flex items-center gap-2 mt-2">
              <input
                type="radio"
                name="goals"
                checked={form.pregnancy_goals === val}
                onChange={() => setForm({ ...form, pregnancy_goals: val })}
              />
              {label}
            </label>
          ))}
        </fieldset>
      )}
      {step === 2 && (
        <label className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={form.breastfeeding}
            onChange={(e) => setForm({ ...form, breastfeeding: e.target.checked })}
          />
          {tr("recommend.breastfeeding")}
        </label>
      )}
      {step === 3 && (
        <fieldset>
          <legend className="text-sm font-medium">{tr("recommend.health")}</legend>
          {["hypertension", "diabetes", "anemia"].map((c) => (
            <label key={c} className="flex items-center gap-2 mt-2 capitalize">
              <input
                type="checkbox"
                checked={form.health_conditions.includes(c)}
                onChange={(e) => {
                  const list = e.target.checked
                    ? [...form.health_conditions, c]
                    : form.health_conditions.filter((x) => x !== c);
                  setForm({ ...form, health_conditions: list });
                }}
              />
              {c}
            </label>
          ))}
        </fieldset>
      )}
      {step === 4 && (
        <fieldset>
          <legend className="text-sm font-medium">{tr("recommend.duration")}</legend>
          {(
            [
              ["short_term", tr("recommend.duration.short")],
              ["medium", tr("recommend.duration.medium")],
              ["long_term", tr("recommend.duration.long")],
            ] as const
          ).map(([val, label]) => (
            <label key={val} className="flex items-center gap-2 mt-2">
              <input
                type="radio"
                name="duration"
                checked={form.preferred_duration === val}
                onChange={() => setForm({ ...form, preferred_duration: val })}
              />
              {label}
            </label>
          ))}
        </fieldset>
      )}
      {step === 5 && (
        <label className="block">
          <span className="text-sm font-medium">{tr("recommend.region")}</span>
          <select
            value={form.region}
            onChange={(e) => setForm({ ...form, region: e.target.value })}
            className="mt-1 w-full rounded-lg border border-care-200 px-3 py-2"
          >
            <option>Kenya</option>
            <option>Ethiopia</option>
            <option>Tanzania</option>
            <option>Uganda</option>
            <option>Nigeria</option>
          </select>
        </label>
      )}

      <div className="flex justify-between pt-2">
        <Button variant="secondary" type="button" onClick={back} disabled={step === 0}>
          {tr("recommend.back")}
        </Button>
        <Button type="button" onClick={next}>
          {step === STEPS - 1 ? tr("recommend.submit") : tr("recommend.next")}
        </Button>
      </div>
    </div>
  );
}
