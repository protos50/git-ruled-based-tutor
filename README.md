# Git Interactive Tutor 🚀

Un asistente inteligente diseñado para enseñar y practicar Git de manera interactiva. Este proyecto combina un chat conversacional con un simulador de terminal realista para explicar conceptos, visualizar el efecto de los comandos y guiar al usuario paso a paso.

## 🌟 Características Principales

- **🤖 Chat Asistente**: Responde dudas sobre comandos, conceptos y flujos de trabajo de Git.
- **🖥️ Simulador de Terminal**: Ejecuta comandos como `git init`, `git commit`, `git merge` en un entorno seguro y visualiza la salida real.
- **📚 Base de Conocimiento**: Explicaciones detalladas, flags comunes y advertencias de errores frecuentes.
- **🌍 Soporte Bilingüe**: Estructura preparada para Español e Inglés.
- **⚡ Feedback Visual**: Interfaz moderna con Next.js que muestra el estado del repositorio simulado.

## 🛠️ Stack Tecnológico

- **Frontend**: 
  - Next.js 15 (App Router)
  - React 19
  - Tailwind CSS
  - Lucide React (Iconos)
- **Backend**: 
  - Python 3.x
  - Flask (API REST)
  - Gestión de datos basada en JSON (sin base de datos pesada)

## 🚀 Cómo Ejecutar el Proyecto

### Prerrequisitos
- Node.js y npm
- Python 3.8+

### 1. Configurar el Backend
```bash
cd backend
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```
El servidor correrá en `http://localhost:5000`.

### 2. Configurar el Frontend
En una nueva terminal:
```bash
cd frontend
npm install
npm run dev
```
Abre `http://localhost:3000` en tu navegador.

## 📂 Estructura del Proyecto

```
├── backend/
│   ├── core/           # Lógica del agente y simulador
│   ├── knowledge/      # Base de conocimiento (JSON)
│   └── app.py          # Punto de entrada Flask
├── frontend/
│   ├── components/     # Componentes React (Chat, Terminal)
│   └── app/            # Páginas Next.js
└── plan_desarollo.md   # Hoja de ruta del proyecto
```

## 🎓 Contexto Académico
Desarrollado como Prototipo 1 para la cátedra de Inteligencia Artificial (TP2).
