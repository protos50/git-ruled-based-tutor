# Git Interactive Tutor 🚀

An intelligent assistant designed to teach and practice Git interactively. This project combines a conversational chat with a realistic terminal simulator to explain concepts, visualize command effects, and guide the user step-by-step.

## 🌟 Key Features

- **🤖 Assistant Chat**: Answers questions about Git commands, concepts, and workflows.
- **🖥️ Terminal Simulator**: Executes commands like `git init`, `git commit`, `git merge` in a safe environment and visualizes real output.
- **📚 Knowledge Base**: Detailed explanations, common flags, and warnings for frequent errors.
- **🌍 Bilingual Support**: Structure prepared for both Spanish and English.
- **⚡ Visual Feedback**: Modern interface built with Next.js that displays the simulated repository state.

## 🛠️ Tech Stack

- **Frontend**: 
  - Next.js 15 (App Router)
  - React 19
  - Tailwind CSS
  - Lucide React (Icons)
- **Backend**: 
  - Python 3.x
  - Flask (REST API)
  - JSON-based data management (no heavy database required)

## 🚀 How to Run

### Prerequisites

- Node.js and npm
- Python 3.8+

### 1. Setup Backend

```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

The server will run at `http://localhost:5000`.

### 2. Setup Frontend

In a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

## 📂 Project Structure

```
├── backend/
│   ├── core/           # Agent logic and simulator
│   ├── knowledge/      # Knowledge base (JSON)
│   └── app.py          # Flask entry point
├── frontend/
│   ├── components/     # React components (Chat, Terminal)
│   └── app/            # Next.js pages
└── plan_desarollo.md   # Project roadmap
```

## 🎓 Academic Context

Developed as Prototype 1 for the Artificial Intelligence course (TP2).

