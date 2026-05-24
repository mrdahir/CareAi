import { api } from "./api";
import type { RecommendRequest, RecommendResponse } from "../types/recommendation";

export async function getRecommendations(
  payload: RecommendRequest
): Promise<RecommendResponse> {
  const { data } = await api.post<RecommendResponse>("/recommend", payload);
  return data;
}
