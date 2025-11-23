"use client"

import { Circle } from "lucide-react"

interface HeaderProps {
  lang: "es" | "en"
  onLangChange: (lang: "es" | "en") => void
  isOnline: boolean
}

export function Header({ lang, onLangChange, isOnline }: HeaderProps) {
  return (
    <header className="border-b border-border px-6 py-4 flex items-center justify-between bg-secondary/30 backdrop-blur-sm">
      <div className="flex items-center gap-3">
        <div className="w-8 h-8 rounded-lg bg-accent flex items-center justify-center font-bold text-foreground">G</div>
        <h1 className="text-2xl font-bold text-foreground">GitMaster AI</h1>
      </div>

      <div className="flex items-center gap-4">
        {/* Status Indicator */}
        <div className="flex items-center gap-2">
          <Circle
            className={`w-2 h-2 ${isOnline ? "fill-green-500 text-green-500" : "fill-yellow-500 text-yellow-500"}`}
          />
          <span className="text-sm text-muted-foreground">
            {isOnline ? (lang === "es" ? "En línea" : "Online") : lang === "es" ? "Conectando..." : "Connecting..."}
          </span>
        </div>

        {/* Language Toggle */}
        <div className="flex gap-1 bg-secondary rounded-lg p-1">
          <button
            onClick={() => onLangChange("es")}
            className={`px-3 py-1.5 text-sm font-medium rounded transition-colors ${
              lang === "es" ? "bg-accent text-accent-foreground" : "text-muted-foreground hover:text-foreground"
            }`}
          >
            ES
          </button>
          <button
            onClick={() => onLangChange("en")}
            className={`px-3 py-1.5 text-sm font-medium rounded transition-colors ${
              lang === "en" ? "bg-accent text-accent-foreground" : "text-muted-foreground hover:text-foreground"
            }`}
          >
            EN
          </button>
        </div>
      </div>
    </header>
  )
}
