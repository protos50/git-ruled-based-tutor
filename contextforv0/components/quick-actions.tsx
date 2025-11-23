"use client"

interface QuickActionsProps {
  lang: "es" | "en"
  onSelect: (action: string) => void
}

export function QuickActions({ lang, onSelect }: QuickActionsProps) {
  const actions = [
    { label: lang === "es" ? "git status" : "git status", value: "git status" },
    { label: lang === "es" ? "git commit" : "git commit", value: "git commit" },
    { label: lang === "es" ? "git branch" : "git branch", value: "git branch" },
    { label: lang === "es" ? "Ayuda" : "Help", value: lang === "es" ? "ayuda" : "help" },
  ]

  return (
    <div className="flex flex-wrap gap-2">
      {actions.map((action) => (
        <button
          key={action.value}
          onClick={() => onSelect(action.value)}
          className="px-4 py-2 text-sm bg-secondary hover:bg-secondary/80 text-foreground border border-border rounded-full transition-colors duration-200 hover:border-accent"
        >
          {action.label}
        </button>
      ))}
    </div>
  )
}
