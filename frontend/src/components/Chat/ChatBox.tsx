import { useState } from "react";
import Card from "../Common/Card";
import ErrorMessage from "../Common/ErrorMessage";
import MessageList from "./MessageList";
import InputBox from "./InputBox";
import { sendChat, streamChat } from "../../services/chatService";
import { useAppStore } from "../../store/useAppStore";
import { useT } from "../../i18n/useT";
import type { ChatMessage } from "../../types/chat";

export default function ChatBox() {
  const { language, userId, setUserId } = useAppStore();
  const tr = useT();
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSend = async (text: string) => {
    setError(null);
    const userMsg: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: text,
    };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);
    const assistantId = crypto.randomUUID();
    setMessages((prev) => [
      ...prev,
      { id: assistantId, role: "assistant", content: "" },
    ]);
    try {
      let streamed = "";
      try {
        await streamChat(
          text,
          language,
          (chunk) => {
            streamed += chunk;
            setMessages((prev) =>
              prev.map((m) =>
                m.id === assistantId ? { ...m, content: streamed } : m
              )
            );
          },
          userId
        );
      } catch {
        const res = await sendChat(text, language, userId);
        if (res.response_id && !userId) {
          setUserId(res.response_id);
        }
        streamed = res.message;
        setMessages((prev) =>
          prev.map((m) =>
            m.id === assistantId
              ? {
                  ...m,
                  id: res.response_id,
                  content: res.message,
                  sources: res.sources,
                }
              : m
          )
        );
        setLoading(false);
        return;
      }
      if (streamed && !userId) {
        setUserId(assistantId);
      }
    } catch (err) {
      setMessages((prev) => prev.filter((m) => m.id !== assistantId));
      setError(err instanceof Error ? err.message : tr("error.generic"));
    } finally {
      setLoading(false);
    }
  };

  const clear = () => {
    setMessages([]);
    setError(null);
  };

  return (
    <Card className="flex flex-col gap-2">
      <div className="flex justify-between items-center">
        <h2 className="text-lg font-semibold text-care-800">{tr("chat.title")}</h2>
        <button
          type="button"
          onClick={clear}
          className="text-xs text-care-600 hover:underline"
        >
          {tr("chat.clear")}
        </button>
      </div>
      {error && <ErrorMessage message={error} />}
      <MessageList messages={messages} loading={loading} />
      <InputBox onSend={handleSend} disabled={loading} />
      <p className="text-xs text-gray-500">{tr("chat.disclaimer")}</p>
    </Card>
  );
}
