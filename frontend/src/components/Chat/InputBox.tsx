import { FormEvent, useState } from "react";
import { Send } from "lucide-react";
import Button from "../Common/Button";
import { useT } from "../../i18n/useT";

const MAX = 2000;

export default function InputBox({
  onSend,
  disabled,
}: {
  onSend: (text: string) => void;
  disabled?: boolean;
}) {
  const tr = useT();
  const [text, setText] = useState("");

  const submit = (e: FormEvent) => {
    e.preventDefault();
    const trimmed = text.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setText("");
  };

  return (
    <form onSubmit={submit} className="flex gap-2 items-end border-t border-care-100 pt-3">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value.slice(0, MAX))}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            submit(e);
          }
        }}
        placeholder={tr("chat.placeholder")}
        rows={2}
        aria-label={tr("chat.placeholder")}
        className="flex-1 resize-none rounded-lg border border-care-200 px-3 py-2 text-sm focus:border-care-500 focus:ring-1 focus:ring-care-500"
        disabled={disabled}
      />
      <Button type="submit" disabled={disabled || !text.trim()} aria-label={tr("chat.send")}>
        <Send className="h-4 w-4" />
      </Button>
      <span className="sr-only">
        {text.length}/{MAX}
      </span>
    </form>
  );
}
