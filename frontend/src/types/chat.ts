export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  sources?: string[];
}

export interface ChatResponse {
  response_id: string;
  message: string;
  sources: string[];
  confidence: number;
  follow_up_suggestions: string[];
  tokens_used: number;
  language_detected: string;
  disclaimer: string;
}
