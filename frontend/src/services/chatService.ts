import { api } from "./api";
import type { ChatResponse } from "../types/chat";

const baseURL = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

export async function sendChat(
  message: string,
  language: string,
  userId?: string | null
): Promise<ChatResponse> {
  const { data } = await api.post<ChatResponse>("/chat", {
    message,
    language,
    user_id: userId || undefined,
  });
  return data;
}

/** Stream assistant text from POST /chat/stream (plain text chunks). */
export async function streamChat(
  message: string,
  language: string,
  onChunk: (chunk: string) => void,
  userId?: string | null
): Promise<void> {
  const res = await fetch(`${baseURL}/chat/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message,
      language,
      user_id: userId || undefined,
    }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(
      (err as { detail?: string }).detail || `Stream failed (${res.status})`
    );
  }
  const reader = res.body?.getReader();
  if (!reader) throw new Error("No response body");
  const decoder = new TextDecoder();
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    onChunk(decoder.decode(value, { stream: true }));
  }
}
