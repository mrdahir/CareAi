import { api } from "./api";

export interface ProgrammeSummary {
  programme: string;
  region: string;
  total_client_visits: number;
  counselled_rate: string;
  top_methods: { method: string; count: number; share: string }[];
  county_count: number;
}

export async function fetchProgrammeSummary(): Promise<ProgrammeSummary> {
  const { data } = await api.get<ProgrammeSummary>("/programme/summary");
  return data;
}
