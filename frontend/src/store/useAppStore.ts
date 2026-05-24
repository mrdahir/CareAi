import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { Language } from "../types/common";

interface AppState {
  language: Language;
  userId: string | null;
  setLanguage: (lang: Language) => void;
  setUserId: (id: string) => void;
}

export const useAppStore = create<AppState>()(
  persist(
    (set) => ({
      language: "en",
      userId: null,
      setLanguage: (language) => set({ language }),
      setUserId: (userId) => set({ userId }),
    }),
    { name: "careapp-store" }
  )
);
