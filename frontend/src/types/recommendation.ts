export interface RecommendRequest {
  age: number;
  breastfeeding: boolean;
  months_postpartum?: number;
  pregnancy_goals: "space_children" | "prevent_pregnancy" | "flexible";
  health_conditions: string[];
  side_effect_tolerance: string[];
  preferred_duration: "short_term" | "medium" | "long_term" | "permanent";
  cost_sensitive?: boolean;
  privacy_needed?: boolean;
  region: string;
  language: string;
}

export interface RecommendationItem {
  rank: number;
  method: string;
  method_id: string;
  match_score: number;
  effectiveness: string;
  duration: string;
  side_effects: string;
  accessibility: string;
  cost: string;
  why_recommended: string[];
  regional_popularity?: string;
  key_reasons: string[];
  next_steps: string;
}

export interface RecommendResponse {
  recommendations: RecommendationItem[];
  survey_questions_answered: number;
  disclaimer: string;
}
