import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "GitMaster AI - Learn Git with AI",
  description: "Interactive Git learning assistant powered by AI. Learn Git commands with explanations and simulations.",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className="dark">
      <body className="font-sans antialiased">
        {children}
      </body>
    </html>
  )
}
