"use client"

import { useEffect, useRef } from "react"
import { MessageBubble } from "./message-bubble"
import type { Message } from "@/types/chat"

interface ChatAreaProps {
  messages: Message[]
  isLoading: boolean
  lang: "es" | "en"
}

export function ChatArea({ messages, isLoading, lang }: ChatAreaProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const endRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  return (
    <div
      ref={containerRef}
      className="flex-1 overflow-y-auto px-6 py-8 space-y-6 bg-gradient-to-b from-background to-background/95"
    >
      {messages.length === 0 ? (
        <div className="h-full flex items-center justify-center">
          <div className="text-center max-w-md">
            <div className="w-16 h-16 rounded-2xl bg-accent/10 flex items-center justify-center mx-auto mb-4">
              <span className="text-3xl">📚</span>
            </div>
            <h2 className="text-2xl font-bold mb-2">
              {lang === "es" ? "Bienvenido a GitMaster AI" : "Welcome to GitMaster AI"}
            </h2>
            <p className="text-muted-foreground">
              {lang === "es"
                ? "Aprende comandos de Git con explicaciones interactivas"
                : "Learn Git commands with interactive explanations"}
            </p>
          </div>
        </div>
      ) : (
        <>
          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-secondary rounded-2xl rounded-tl-sm px-6 py-4 max-w-xs">
                <div className="flex gap-2">
                  <div className="w-2 h-2 bg-muted-foreground rounded-full animate-bounce" />
                  <div className="w-2 h-2 bg-muted-foreground rounded-full animate-bounce delay-100" />
                  <div className="w-2 h-2 bg-muted-foreground rounded-full animate-bounce delay-200" />
                </div>
              </div>
            </div>
          )}
          <div ref={endRef} />
        </>
      )}
    </div>
  )
}
