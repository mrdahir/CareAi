import type { ChatMessage as Msg } from "../../types/chat";

export default function Message({ message }: { message: Msg }) {
  const isUser = message.role === "user";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[85%] rounded-2xl px-4 py-2 text-sm ${
          isUser
            ? "bg-care-600 text-white rounded-br-sm"
            : "bg-white border border-care-100 text-gray-800 rounded-bl-sm"
        }`}
      >
        <p className="whitespace-pre-wrap">{message.content}</p>
        {!isUser && message.sources && message.sources.length > 0 && (
          <p className="mt-2 text-xs opacity-70">
            Sources: {message.sources.join(", ")}
          </p>
        )}
      </div>
    </div>
  );
}
