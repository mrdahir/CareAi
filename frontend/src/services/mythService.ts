import { api } from "./api";

export interface MythCheckResponse {
  is_myth: boolean;
  severity: string;
  myth: string;
  fact: string;
  evidence: string;
  sources: string[];
  similar_myths: string[];
  confidence: number;
}

export async function checkMyth(
  statement: string,
  language: string
): Promise<MythCheckResponse> {
  const { data } = await api.post<MythCheckResponse>("/myth-check", {
    statement,
    language,
  });
  return data;
}
