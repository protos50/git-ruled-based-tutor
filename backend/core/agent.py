import json
from pathlib import Path
from .rules import GIT_RULES as GIT_RULES_ES, DEFAULT_RESPONSE as DEFAULT_RESPONSE_ES
try:
    from .rules_en import GIT_RULES as GIT_RULES_EN, DEFAULT_RESPONSE as DEFAULT_RESPONSE_EN
except Exception:
    GIT_RULES_EN = None
    DEFAULT_RESPONSE_EN = None
from .simulator import GitSimulator

class GitAgent:
    def __init__(self):
        self.rules_es = GIT_RULES_ES
        self.rules_en = GIT_RULES_EN or {}
        self.default_response_es = DEFAULT_RESPONSE_ES
        self.default_response_en = DEFAULT_RESPONSE_EN or "[ES to EN – pending native translation]\n" + DEFAULT_RESPONSE_ES
        self.sessions = {}  # {session_id: context}
        self.session_data = {}  # {session_id: {temp_data}}
        self.simulator = GitSimulator()
        # knowledge_base: lista de items bilingües o monolingües
        self.knowledge_base = self._load_knowledge_base()

    def _load_knowledge_base(self):
        """Carga la base de conocimiento (acepta formato original o bilingüe).
        Formato original: campos en español.
        Formato bilingüe esperado:
        {
          "command": ..., "tags": [...], "i18n": {"es": {...}, "en": {...}}, ...
        }
        """
        try:
            # Ajuste de ruta: backend/core/agent.py -> backend/knowledge/git_knowledge_master.json
            json_path = Path(__file__).resolve().parent.parent / 'knowledge' / 'git_knowledge_master.json'
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data
        except Exception as e:
            print(f"Error cargando knowledge base: {e}")
        return []

    def get_response(self, user_input, session_id="default", lang="es"):
        """
        Analiza la entrada del usuario con prioridad:
        1. Simulación
        2. Menú Dinámico JSON (si está activo)
        3. Búsqueda en JSON
        4. Reglas estáticas (rules.py)
        """
        if not user_input:
            return self.default_response_es if lang == 'es' else self.default_response_en

        text = user_input.lower().strip()
        
        # 0. Inicializar sesión si no existe
        if session_id not in self.sessions:
            self.sessions[session_id] = "main"
            self.session_data[session_id] = {}

        # 1. Comandos de Simulación
        if "simular" in text or "simulate" in text:
            if "head" in text:
                if "detached" in text:
                    return self.simulator.explain_head("detached")
                else:
                    return self.simulator.explain_head("on_branch")
            cmd_match = text.replace("simular", "").strip()
            sim_response = self.simulator.simulate_command(cmd_match)
            if sim_response:
                return sim_response

        # 2. Manejo de Menú Dinámico JSON (Contexto: json_selected)
        current_context = self.sessions.get(session_id, "main")
        
        if current_context == "json_selected":
            # Si el usuario quiere salir
            if text in ["menu", "salir", "inicio", "volver", "ayuda"]:
                self.sessions[session_id] = "main"
                self.session_data[session_id] = {}
                return self._find_match("menu", "main", session_id, lang=lang)
                
            # Procesar opción del submenú JSON
            return self._handle_json_menu_selection(text, session_id, lang=lang)

        # 3. Búsqueda en Knowledge Base (JSON)
        # Solo buscamos si NO estamos en un flujo de menú estático específico (salvo main)
        if current_context == "main":
            kb_response = self._search_knowledge_base(text, session_id, lang=lang)
            if kb_response:
                return kb_response

        # 4. Lógica de Reglas Estáticas (Legacy/Menús)
        if text in ["menu", "salir", "inicio", "volver", "ayuda"]:
            # Si pide ayuda explícitamente, mostramos la ayuda dinámica combinada
            if text == "ayuda" or (lang == 'en' and text in ["help", "menu", "start", "home", "back", "exit"]):
                return self._generate_dynamic_help(lang=lang)
                
            self.sessions[session_id] = "main"
            return self._find_match("menu", "main", session_id, lang=lang)

        response = self._find_match(text, current_context, session_id, lang=lang)
        if response:
            return response
            
        # Fallback a main si se perdió el contexto
        if current_context != "main":
            response = self._find_match(text, "main", session_id, lang=lang)
            if response:
                return response

        return self.default_response_es if lang == 'es' else self.default_response_en


    def _search_knowledge_base(self, text, session_id, lang="es"):
        """Busca en el JSON. Si encuentra, activa el menú dinámico."""
        best_match = None
        max_score = 0

        for item in self.knowledge_base:
            score = 0
            # Coincidencia exacta de comando
            if item['command'] == text:
                score += 100
            # Coincidencia parcial: comando en texto O texto en comando
            elif item['command'] in text or text in item['command']:
                score += 50
            
            for tag in item.get('tags', []):
                if tag in text:
                    score += 20
            
            if score > max_score and score > 0:
                max_score = score
                best_match = item

        if best_match and max_score > 0:
            # Guardamos el item seleccionado en la sesión
            self.sessions[session_id] = "json_selected"
            self.session_data[session_id] = {'item': best_match}
            
            # Retornamos el menú inicial del item
            return self._format_json_menu_intro(best_match, lang=lang)
        
        return None

    def _format_json_menu_intro(self, item, lang="es"):
        """Muestra la introducción y opciones disponibles para un comando JSON."""
        # Compatibilidad con formato bilingüe
        simple = None
        if 'i18n' in item:
            simple = item['i18n'].get(lang, {}).get('simple_explanation')
        if not simple:
            simple = item.get('simple_explanation')

        if lang == 'en':
            menu = (
                f"📚 **{item['command'].upper()}**\n\n"
                f"{simple}\n\n"
                "What would you like to know?\n"
                "1. 💡 Detailed explanation\n"
                "2. 🚩 Common flags and options\n"
                "3. 📝 Usage examples\n"
                "4. ⚠️ Common pitfalls\n"
            )
            if self.simulator.simulate_command(item['command']):
                menu += "5. 🕹️ Simulate this command\n"
                menu += "6. 🔙 Back to main menu"
            else:
                menu += "5. 🔙 Back to main menu"
        else:
            menu = (
                f"📚 **{item['command'].upper()}**\n\n"
                f"{simple}\n\n"
                "¿Qué deseas saber?\n"
                "1. 💡 Explicación detallada\n"
                "2. 🚩 Flags y opciones comunes\n"
                "3. 📝 Ejemplos de uso\n"
                "4. ⚠️ Errores comunes\n"
            )
            
            # Verificar si el comando tiene simulación disponible
            if self.simulator.simulate_command(item['command']):
                menu += "5. 🕹️ Simular este comando\n"
                menu += "6. 🔙 Volver al menú principal"
            else:
                menu += "5. 🔙 Volver al menú principal"
            
        return menu

    def _handle_json_menu_selection(self, text, session_id, lang="es"):
        """Procesa la selección numérica dentro de un item JSON."""
        item = self.session_data[session_id].get('item')
        if not item:
            self.sessions[session_id] = "main"
            return "❌ Error de sesión. Volviendo al inicio." if lang == 'es' else "❌ Session error. Returning to start."

        has_sim = self.simulator.simulate_command(item['command']) is not None

        if text == "1":
            deep = None
            if 'i18n' in item:
                deep = item['i18n'].get(lang, {}).get('deep_explanation')
            if not deep:
                deep = item.get('deep_explanation')
            
            header = f"💡 **Detalle de {item['command']}**" if lang == 'es' else f"💡 **Details of {item['command']}**"
            fallback_msg = 'No hay explicación detallada disponible.' if lang == 'es' else 'No detailed explanation available.'
            footer = "(Escribe otra opción o 'menu' para salir)" if lang == 'es' else "(Type another option or 'menu' to exit)"
            
            return f"{header}\n\n{deep or fallback_msg}\n\n{footer}"

        elif text == "2":
            header = "🚩 **Opciones Comunes:**\n" if lang == 'es' else "🚩 **Common Options:**\n"
            # Preferir flags por idioma si existen
            flags = None
            if 'i18n' in item:
                flags = item['i18n'].get(lang, {}).get('flags')
            if not flags:
                flags = item.get('flags')

            flags_text = header
            if flags:
                for flag in flags:
                    flags_text += f"- `{flag['flag']}`: {flag['description']}\n"
            else:
                flags_text += "No hay flags registradas." if lang == 'es' else "No flags registered."
            
            footer = "\n(Escribe otra opción o 'menu' para salir)" if lang == 'es' else "\n(Type another option or 'menu' to exit)"
            return flags_text + footer

        elif text == "3":
            header = "📝 **Ejemplos:**\n" if lang == 'es' else "📝 **Examples:**\n"
            # Preferir ejemplos por idioma si existen
            examples = None
            if 'i18n' in item:
                examples = item['i18n'].get(lang, {}).get('examples')
            if not examples:
                examples = item.get('examples')

            ex_text = header
            if examples:
                for ex in examples:
                    ex_text += f"- `{ex}`\n"
            else:
                ex_text += "No hay ejemplos registrados." if lang == 'es' else "No examples registered."
            
            footer = "\n(Escribe otra opción o 'menu' para salir)" if lang == 'es' else "\n(Type another option or 'menu' to exit)"
            return ex_text + footer

        elif text == "4":
            pitfalls = None
            if 'i18n' in item:
                pitfalls = item['i18n'].get(lang, {}).get('common_pitfalls')
            if not pitfalls:
                pitfalls = item.get('common_pitfalls')
            
            header = "⚠️ **Cuidado:**" if lang == 'es' else "⚠️ **Warning:**"
            fallback_msg = 'No hay errores comunes registrados.' if lang == 'es' else 'No common pitfalls registered.'
            footer = "\n\n(Escribe otra opción o 'menu' para salir)" if lang == 'es' else "\n\n(Type another option or 'menu' to exit)"
            
            return f"{header}\n{pitfalls or fallback_msg}{footer}"
        
        # Lógica para opción 5 (Simular o Salir)
        elif text == "5":
            if has_sim:
                footer = "\n\n(Escribe otra opción o 'menu' para salir)" if lang == 'es' else "\n\n(Type another option or 'menu' to exit)"
                return self.simulator.simulate_command(item['command']) + footer
            else:
                self.sessions[session_id] = "main"
                self.session_data[session_id] = {}
                return "🔙 Volviendo al menú principal..." if lang == 'es' else "🔙 Returning to main menu..."
        
        # Lógica para opción 6 (Salir si hay simulación)
        elif text == "6" and has_sim:
            self.sessions[session_id] = "main"
            self.session_data[session_id] = {}
            return "🔙 Volviendo al menú principal..." if lang == 'es' else "🔙 Returning to main menu..."
            
        else:
            max_opt = "6" if has_sim else "5"
            msg = f"❓ Opción no válida. Elige un número del 1 al {max_opt}." if lang == 'es' else f"❓ Invalid option. Choose a number from 1 to {max_opt}."
            return msg

    def _generate_dynamic_help(self, lang="es"):
        """Genera una lista de todos los comandos disponibles en el JSON."""
        categories = {}
        for item in self.knowledge_base:
            cat = item.get('category', 'Otros')
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item['command'])
        
        title = "🎓 **Ayuda Dinámica - Comandos Disponibles**\n\n" if lang == 'es' else "🎓 **Dynamic Help - Available Commands**\n\n"
        help_text = title
        for cat, cmds in categories.items():
            help_text += f"**{cat}:**\n"
            help_text += ", ".join([f"`{c}`" for c in cmds]) + "\n\n"
            
        help_text += "Escribe cualquiera de estos comandos para aprender más." if lang == 'es' else "Type any of these commands to learn more."
        return help_text

    def _find_match(self, text, context, session_id="default", lang="es"):
        """Busca una regla coincidente en un contexto específico (Legacy)"""
        rules = self.rules_es if lang == 'es' else (self.rules_en or {})
        context_rules = rules.get(context, [])
        for keyword, response, next_context in context_rules:
            if text.isdigit():
                if keyword == text:
                    self.sessions[session_id] = next_context
                    return response
            elif keyword in text:
                self.sessions[session_id] = next_context
                return response
        return None

    def _simple_translate(self, text: str) -> str:
        """Traducción mínima placeholder para reglas estáticas.
        Se recomienda reemplazar con contenido nativo en inglés.
        """
        # Estrategia: devolver texto original con aviso.
        return "[ES to EN – pending native translation]\n" + text
