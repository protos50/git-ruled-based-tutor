"use client"

import type React from "react"

import { useState } from "react"
import { Send } from "lucide-react"
import { QuickActions } from "./quick-actions"

interface InputAreaProps {
  onSendMessage: (text: string) => void
  onQuickAction: (action: string) => void
  isLoading: boolean
  lang: "es" | "en"
}

export function InputArea({ onSendMessage, onQuickAction, isLoading, lang }: InputAreaProps) {
  const [input, setInput] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim() && !isLoading) {
      onSendMessage(input)
      setInput("")
    }
  }

  return (
    <div className="border-t border-border bg-secondary/30 backdrop-blur-sm p-6 space-y-4">
      <QuickActions lang={lang} onSelect={onQuickAction} />

      <form onSubmit={handleSubmit} className="flex gap-3">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={isLoading}
          placeholder={lang === "es" ? "Pregunta sobre un comando de Git..." : "Ask about a Git command..."}
          className="flex-1 bg-background border border-border rounded-lg px-4 py-3 text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-accent transition-all disabled:opacity-50 disabled:cursor-not-allowed"
        />
        <button
          type="submit"
          disabled={isLoading || !input.trim()}
          className="bg-accent hover:bg-accent/90 disabled:bg-accent/50 text-accent-foreground rounded-lg px-4 py-3 font-medium flex items-center gap-2 transition-all disabled:cursor-not-allowed"
        >
          <Send className="w-4 h-4" />
          <span className="hidden sm:inline">{lang === "es" ? "Enviar" : "Send"}</span>
        </button>
      </form>
    </div>
  )
}
