"use client"

import ReactMarkdown from "react-markdown"
import type { Message } from "@/types/chat"

interface MessageBubbleProps {
  message: Message
}

export function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.type === "user"

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-3xl rounded-2xl px-6 py-4 ${
          isUser ? "bg-accent text-accent-foreground rounded-tr-sm" : "bg-secondary text-foreground rounded-tl-sm"
        }`}
      >
        {isUser ? (
          <p className="text-lg leading-relaxed">{message.content}</p>
        ) : (
          <div className="prose prose-invert max-w-none text-lg">
            <ReactMarkdown
              components={{
                p: ({ children }) => <p className="mb-2 leading-relaxed">{children}</p>,
                h1: ({ children }) => <h1 className="text-2xl font-bold mb-3 mt-3">{children}</h1>,
                h2: ({ children }) => <h2 className="text-xl font-bold mb-2 mt-2">{children}</h2>,
                h3: ({ children }) => <h3 className="text-lg font-bold mb-2">{children}</h3>,
                ul: ({ children }) => <ul className="list-disc list-inside mb-2 space-y-0.5">{children}</ul>,
                ol: ({ children }) => <ol className="list-decimal list-inside mb-2 space-y-0.5">{children}</ol>,
                li: ({ children }) => <li className="ml-2 leading-relaxed">{children}</li>,
                code: ({ children, className }) => {
                  const isInline = !className
                  return isInline ? (
                    <code className="bg-background/50 px-2 py-0.5 rounded text-accent font-mono text-base">
                      {children}
                    </code>
                  ) : (
                    <code className="block bg-background/50 p-3 rounded-lg font-mono text-base mb-2 overflow-x-auto border border-border">
                      {children}
                    </code>
                  )
                },
                pre: ({ children }) => <pre className="mb-2">{children}</pre>,
                strong: ({ children }) => <strong className="font-bold text-accent">{children}</strong>,
                em: ({ children }) => <em className="italic">{children}</em>,
              }}
            >
              {message.content}
            </ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  )
}
