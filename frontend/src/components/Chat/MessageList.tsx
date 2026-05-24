import { useEffect, useRef } from "react";
import type { ChatMessage } from "../../types/chat";
import Message from "./Message";
import Loading from "../Common/Loading";

export default function MessageList({
  messages,
  loading,
}: {
  messages: ChatMessage[];
  loading: boolean;
}) {
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="flex flex-col gap-3 min-h-[320px] max-h-[50vh] overflow-y-auto p-2">
      {messages.length === 0 && (
        <p className="text-center text-gray-500 text-sm py-8">
          Ask a question about contraception, breastfeeding, or family planning.
        </p>
      )}
      {messages.map((m) => (
        <Message key={m.id} message={m} />
      ))}
      {loading && <Loading label="CareApp is thinking..." />}
      <div ref={endRef} />
    </div>
  );
}
