import json
from pathlib import Path

class GitSimulator:
    def __init__(self):
        self.simulations = self._load_simulations()

    def _load_simulations(self):
        """Carga las simulaciones desde el archivo JSON."""
        try:
            json_path = Path(__file__).resolve().parent.parent / 'knowledge' / 'git_simulations.json'
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error cargando simulaciones: {e}")
        return {}

    def explain_head(self, state):
        """
        Simula una explicación del agente basada en dónde está el HEAD.
        state puede ser: 'on_branch' o 'detached'
        """
        if state == 'on_branch':
            return (
                "📍 **Simulación: HEAD en Rama**\n\n"
                "Tu HEAD está apuntando a una rama (ej: `main`).\n"
                "Todo commit que hagas hará crecer esta rama automáticamente.\n"
                "Es como escribir en la última página de tu cuaderno."
            )
        elif state == 'detached':
            return (
                "⚠️ **Simulación: Detached HEAD**\n\n"
                "Tu HEAD está apuntando directamente a un commit antiguo, no a una rama.\n"
                "Es como si hubieras viajado en el tiempo a ver una foto vieja.\n\n"
                "⛔ **Si haces commit aquí:** Se guardará, PERO si luego cambias a 'main', este commit quedará 'huérfano' y se borrará.\n"
                "✅ **Solución:** Si quieres guardar cambios aquí, crea una rama nueva ya mismo: `git switch -c mi-experimento`."
            )
        else:
            return "❓ Estado de HEAD desconocido. Intenta 'on_branch' o 'detached'."

    def simulate_command(self, command, lang="es"):
        """
        Simula la salida o efecto de un comando específico usando el JSON.
        """
        cmd = command.lower().strip()
        
        # Casos especiales que no están en el JSON o requieren lógica extra
        if cmd == "concept: head" or cmd == "head":
            return self.explain_head('on_branch') + "\n\n(Para ver el caso peligroso, escribe: `simular head detached`)"

        # Lógica para git checkout / switch dinámico
        if "git checkout" in cmd or "git switch" in cmd:
            branch_name = cmd.split()[-1] if len(cmd.split()) > 2 else "feature-login"
            sim_data = self.simulations.get("git checkout")
            if sim_data:
                terminal = sim_data["terminal"].replace("{branch_name}", branch_name)
                analysis = sim_data["analysis"].get(lang, sim_data["analysis"]["es"]).replace("{branch_name}", branch_name)
                return f"🖥️ **Simulación de Terminal:**\n```bash\n{terminal}\n```\n💡 **Análisis:** {analysis}"

        # Búsqueda en el JSON
        # Intentamos coincidencia exacta primero
        sim_data = self.simulations.get(cmd)
        
        # Si no, buscamos si alguna clave del JSON está contenida en el comando
        if not sim_data:
            for key, data in self.simulations.items():
                if key in cmd:
                    sim_data = data
                    break
        
        if sim_data:
            terminal = sim_data["terminal"]
            analysis = sim_data["analysis"].get(lang, sim_data["analysis"]["es"])
            
            # Detectar lenguaje del bloque de código (bash por defecto, diff para git diff)
            code_lang = "diff" if "diff" in cmd else "bash"
            
            return f"🖥️ **Simulación de Terminal:**\n```{code_lang}\n{terminal}\n```\n💡 **Análisis:** {analysis}"
            
        return None
