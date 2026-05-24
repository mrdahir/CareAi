import { useAppStore } from "../store/useAppStore";
import { t, type TranslationKey } from "./translations";

export function useT() {
  const language = useAppStore((s) => s.language);
  return (key: TranslationKey) => t(language, key);
}
