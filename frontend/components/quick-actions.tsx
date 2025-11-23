"use client"

interface QuickActionsProps {
  lang: "es" | "en"
  onSelect: (action: string) => void
}

export function QuickActions({ lang, onSelect }: QuickActionsProps) {
  const actions = [
    { label: "git status", value: "git status" },
    { label: "git commit", value: "git commit" },
    { label: "git branch", value: "git branch" },
    { label: lang === "es" ? "Menú" : "Menu", value: "menu" },
    { label: lang === "es" ? "Ayuda" : "Help", value: lang === "es" ? "ayuda" : "help" },
  ]

  return (
    <div className="flex flex-wrap gap-2">
      {actions.map((action) => (
        <button
          key={action.value}
          onClick={() => onSelect(action.value)}
          className="px-5 py-2.5 text-base bg-secondary hover:bg-secondary/80 text-foreground border border-border rounded-full transition-colors duration-200 hover:border-accent"
        >
          {action.label}
        </button>
      ))}
    </div>
  )
}
