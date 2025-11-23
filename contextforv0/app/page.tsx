"use client"

import { useState, useRef, useEffect } from "react"
import { ChatArea } from "@/components/chat-area"
import { InputArea } from "@/components/input-area"
import { Header } from "@/components/header"
import type { Message } from "@/types/chat"

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000"

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [lang, setLang] = useState<"es" | "en">("es")
  const [isOnline, setIsOnline] = useState(true)
  const sessionIdRef = useRef(`session-${Date.now()}`)

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/health`)
        setIsOnline(response.ok)
      } catch {
        setIsOnline(false)
      }
    }

    checkHealth()
    const interval = setInterval(checkHealth, 30000)
    return () => clearInterval(interval)
  }, [])

  const handleSendMessage = async (text: string) => {
    if (!text.trim()) return

    const userMessage: Message = {
      id: `msg-${Date.now()}`,
      type: "user",
      content: text,
      timestamp: new Date(),
    }

    setMessages((prev) => [...prev, userMessage])
    setIsLoading(true)

    try {
      const response = await fetch(`${API_BASE_URL}/api/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: text,
          session_id: sessionIdRef.current,
          lang: lang,
        }),
      })

      if (!response.ok) throw new Error("API Error")

      const data = await response.json()
      const aiMessage: Message = {
        id: `msg-${Date.now()}-ai`,
        type: "ai",
        content: data.response,
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, aiMessage])
    } catch (error) {
      console.error("Error:", error)
      const errorMessage: Message = {
        id: `msg-${Date.now()}-error`,
        type: "ai",
        content:
          lang === "es"
            ? "❌ Error al conectar con el servidor. Por favor, intenta de nuevo."
            : "❌ Error connecting to server. Please try again.",
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleQuickAction = (action: string) => {
    handleSendMessage(action)
  }

  return (
    <div className="flex flex-col h-screen bg-background text-foreground">
      <Header lang={lang} onLangChange={setLang} isOnline={isOnline} />
      <ChatArea messages={messages} isLoading={isLoading} lang={lang} />
      <InputArea
        onSendMessage={handleSendMessage}
        onQuickAction={handleQuickAction}
        isLoading={isLoading}
        lang={lang}
      />
    </div>
  )
}
