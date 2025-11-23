"use client"

import React, { useState, useRef, useEffect } from "react"
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
  const inputRef = useRef<HTMLInputElement>(null)

  // Recuperar el foco automáticamente cuando termina de cargar (isLoading pasa a false)
  useEffect(() => {
    if (!isLoading) {
      // Pequeño delay para asegurar que el atributo disabled se ha quitado del DOM
      // Aumentado a 50ms para mayor compatibilidad entre navegadores
      const timer = setTimeout(() => {
        inputRef.current?.focus()
      }, 50)
      return () => clearTimeout(timer)
    }
  }, [isLoading])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim() && !isLoading) {
      const message = input
      setInput("")
      onSendMessage(message)
    }
  }

  const handleQuickActionClick = (action: string) => {
    onQuickAction(action)
  }

  return (
    <div className="border-t border-border bg-secondary/30 backdrop-blur-sm p-6 space-y-4">
      <QuickActions lang={lang} onSelect={handleQuickActionClick} />

      <form onSubmit={handleSubmit} className="flex gap-3">
        <input
          ref={inputRef}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={isLoading}
          autoFocus
          autoComplete="off"
          placeholder={lang === "es" ? "Pregunta sobre un comando de Git..." : "Ask about a Git command..."}
          className="flex-1 bg-background border border-border rounded-lg px-4 py-4 text-lg text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-accent transition-all disabled:opacity-50 disabled:cursor-not-allowed"
        />
        <button
          type="submit"
          disabled={isLoading || !input.trim()}
          className="bg-accent hover:bg-accent/90 disabled:bg-accent/50 text-accent-foreground rounded-lg px-6 py-4 font-medium flex items-center gap-2 transition-all disabled:cursor-not-allowed"
        >
          <Send className="w-5 h-5" />
          <span className="hidden sm:inline text-lg">{lang === "es" ? "Enviar" : "Send"}</span>
        </button>
      </form>
    </div>
  )
}
