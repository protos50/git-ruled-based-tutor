# Definición de reglas para el Agente de Git (Nivel Profesional)
# Estructura:
# RULES = {
#     "context_name": [
#         ("keyword", "response", "next_context")
#     ]
# }

GIT_RULES = {
    "main": [
        ("status",
         "📊 **Estado del Repositorio (git status)**\n\n"
         "El comando `git status` es fundamental para entender qué está pasando.\n"
         "¿Qué variante deseas conocer?\n\n"
         "1. `git status` (Estándar - Detallado)\n"
         "2. `git status -s` (Short - Resumido)\n"
         "3. `git status -sb` (Short + Branch info)\n"
         "4. Volver al menú principal",
         "status_menu"),

        ("log",
         "� **Historial de Cambios (git log)**\n\n"
         "Visualiza la historia de tu proyecto.\n"
         "Opciones recomendadas:\n\n"
         "1. `git log` (Estándar)\n"
         "2. `git log --oneline` (Resumido en una línea)\n"
         "3. `git log --graph --oneline --all` (Gráfico visual de ramas)\n"
         "4. `git log -p` (Muestra cambios/diffs en cada commit)\n"
         "5. Volver al menú principal",
         "log_menu"),

        ("commit",
         "💾 **Guardando Cambios (git commit)**\n\n"
         "Crea un punto en la historia del proyecto.\n"
         "Variantes útiles:\n\n"
         "1. `git commit -m 'mensaje'` (Estándar)\n"
         "2. `git commit -am 'mensaje'` (Add + Commit de archivos trackeados)\n"
         "3. `git commit --amend` (Corregir el último commit)\n"
         "4. Volver al menú principal",
         "commit_menu"),

        ("diff",
         "🔍 **Inspección de Cambios (git diff)**\n\n"
         "Compara versiones de tu código.\n"
         "¿Qué quieres comparar?\n\n"
         "1. `git diff` (Working Directory vs Staging Area)\n"
         "2. `git diff --staged` (Staging Area vs Último Commit)\n"
         "3. `git diff HEAD` (Working Directory vs Último Commit)\n"
         "4. Volver al menú principal",
         "diff_menu"),

        ("conflict", 
         "🔧 **Gestión de Conflictos**\n\n"
         "Los conflictos ocurren cuando Git no puede fusionar cambios automáticamente.\n"
         "¿Qué tipo de conflicto tienes?\n\n"
         "1. Conflicto de contenido (líneas modificadas por ambos)\n"
         "2. Archivo eliminado por uno y modificado por otro\n"
         "3. Volver al menú principal",
         "conflict_menu"),
        
        ("push",
         "🚀 **Subir Cambios (git push)**\n\n"
         "Envía tus commits al repositorio remoto.\n"
         "Selecciona tu problema o variante:\n\n"
         "1. Push Rejected (non-fast-forward)\n"
         "2. `git push -u origin <rama>` (Establecer upstream)\n"
         "3. `git push --force` (⚠️ Peligroso: Sobrescribir historia)\n"
         "4. Volver al menú principal",
         "push_menu"),
        
        ("branch",
         "🌿 **Gestión de Ramas (git branch)**\n\n"
         "Las ramas permiten trabajar en paralelo.\n"
         "¿Qué deseas hacer?\n\n"
         "1. Crear una rama nueva\n"
         "2. Cambiar de rama (checkout/switch)\n"
         "3. Listar ramas\n"
         "4. Borrar una rama\n"
         "5. Volver al menú principal",
         "branch_menu"),
         
        ("profesional",
         "👨‍💻 **Derivando a un Instructor...**\n\n"
         "Entiendo que necesitas asistencia personalizada para tu curso.\n"
         "Un instructor revisará tu caso. Por favor, describe el problema detalladamente en el canal de soporte del curso.\n\n"
         "(Escribe 'menu' para volver)",
         "main"),
         
        ("ayuda",
         "🎓 **Asistente Educativo Git - Menú Principal**\n\n"
         "Estoy aquí para ayudarte en tu aprendizaje. Temas disponibles:\n\n"
         "- **Estado:** `status`\n"
         "- **Historial:** `log`\n"
         "- **Cambios:** `diff`\n"
         "- **Guardar:** `commit`\n"
         "- **Ramas:** `branch`\n"
         "- **Conflictos:** `conflict`\n"
         "- **Remoto:** `push`\n\n"
         "Escribe el comando o tema que te interesa.",
         "main"),
         
        ("menu",
         "🔙 **Menú Principal**\n\n"
         "¿Qué tema quieres repasar hoy? (status, log, commit, diff, branch...)",
         "main")
    ],

    # --- SUBMENÚS ---

    "status_menu": [
        ("1", 
         "📊 **git status**\n\n"
         "Muestra el estado del árbol de trabajo (working directory).\n"
         "- Archivos modificados no preparados (rojo)\n"
         "- Archivos preparados para commit (verde)\n"
         "- Archivos sin seguimiento (untracked)\n\n"
         "Es el comando que deberías ejecutar más frecuentemente.", 
         "main"),
        ("2",
         "📊 **git status -s** (Short)\n\n"
         "Muestra una salida compacta, ideal para scripts o vista rápida.\n"
         "- `M ` (verde): Modificado en staging\n"
         "- ` M` (rojo): Modificado en working dir\n"
         "- `??`: Untracked",
         "main"),
        ("3",
         "📊 **git status -sb** (Short + Branch)\n\n"
         "Combina la vista corta (`-s`) con información de la rama actual (`-b`).\n"
         "Te dice en qué rama estás y si estás por delante/detrás del remoto (ahead/behind).\n\n"
         "Ejemplo de salida:\n"
         "`## main...origin/main [ahead 1]`",
         "main"),
        ("4", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ],

    "log_menu": [
        ("1",
         "� **git log**\n\n"
         "Muestra el historial completo de commits (hash, autor, fecha, mensaje).\n"
         "Usa las flechas para navegar y `q` para salir del paginador.",
         "main"),
        ("2",
         "📜 **git log --oneline**\n\n"
         "Muestra cada commit en una sola línea con el hash corto y el título.\n"
         "Ideal para tener un panorama general de la historia reciente.",
         "main"),
        ("3",
         "📜 **git log --graph --oneline --all**\n\n"
         "El comando definitivo para visualizar ramificaciones y fusiones en la terminal.\n"
         "- `--graph`: Dibuja líneas ASCII conectando commits.\n"
         "- `--all`: Muestra todas las ramas, no solo la actual.",
         "main"),
        ("4",
         "📜 **git log -p** (Patch)\n\n"
         "Muestra no solo el mensaje del commit, sino también el **diff** (los cambios exactos) introducidos en cada commit.\n"
         "Útil para revisión de código (code review).",
         "main"),
        ("5", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ],

    "commit_menu": [
        ("1",
         "� **git commit -m 'mensaje'**\n\n"
         "Crea un commit con los archivos que están en el área de preparación (staging area).\n"
         "Recuerda usar mensajes descriptivos e imperativos (ej: 'Agregar validación de usuario').",
         "main"),
        ("2",
         "💾 **git commit -am 'mensaje'**\n\n"
         "Atajo que combina `git add` (para archivos ya trackeados) y `git commit`.\n"
         "⚠️ Cuidado: No incluye archivos nuevos (untracked), solo modificados.",
         "main"),
        ("3",
         "💾 **git commit --amend**\n\n"
         "Permite modificar el **último** commit.\n"
         "- Si olvidaste agregar un archivo: haz `git add` y luego `git commit --amend`.\n"
         "- Si quieres cambiar el mensaje: ejecútalo y edita el texto.\n"
         "⚠️ No uses esto si ya hiciste push del commit (reescribe la historia).",
         "main"),
        ("4", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ],

    "diff_menu": [
        ("1",
         "� **git diff**\n\n"
         "Muestra los cambios en tu directorio de trabajo que **NO** han sido agregados al staging area.\n"
         "Es lo que perderías si hicieras un `git checkout .`",
         "main"),
        ("2",
         "🔍 **git diff --staged** (o --cached)\n\n"
         "Muestra los cambios que **SÍ** están en el staging area y que irán en el próximo commit.\n"
         "Siempre revisa esto antes de hacer commit.",
         "main"),
        ("3",
         "🔍 **git diff HEAD**\n\n"
         "Muestra todos los cambios (staged + unstaged) comparados con el último commit.",
         "main"),
        ("4", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ],
    
    "conflict_menu": [
        ("1", 
         "📝 **Conflicto de Contenido**\n\n"
         "1. Ejecuta `git status` para ver archivos en conflicto.\n"
         "2. Abre los archivos y busca las marcas `<<<<<<<`, `=======`, `>>>>>>>`.\n"
         "3. Edita el código para dejar la versión final correcta.\n"
         "4. Elimina las marcas de conflicto.\n"
         "5. `git add <archivo>` para marcarlo como resuelto.\n"
         "6. `git commit` para finalizar el merge.", 
         "main"),
        ("2",
         "🗑️ **Conflicto Modificado/Eliminado**\n\n"
         "Un usuario modificó un archivo que otro eliminó.\n"
         "- Para mantener el archivo modificado: `git add <archivo>`\n"
         "- Para confirmar la eliminación: `git rm <archivo>`\n"
         "Luego haz commit.",
         "main"),
        ("3", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ],
    
    "push_menu": [
        ("1",
         "🚫 **Push Rejected (Non-fast-forward)**\n\n"
         "Alguien más subió cambios a la misma rama.\n"
         "Solución estándar:\n"
         "1. `git pull --rebase origin <rama>` (Trae cambios y reaplica los tuyos encima)\n"
         "2. Si hay conflictos, resuélvelos y `git rebase --continue`\n"
         "3. `git push origin <rama>`",
         "main"),
        ("2",
         "� **git push -u origin <rama>**\n\n"
         "La opción `-u` (upstream) vincula tu rama local con la remota.\n"
         "En el futuro podrás hacer solo `git push` o `git pull` sin argumentos.",
         "main"),
        ("3",
         "⚠️ **git push --force**\n\n"
         "Fuerza la subida sobrescribiendo la historia remota.\n"
         "**Solo úsalo si:**\n"
         "- Eres la única persona trabajando en esa rama.\n"
         "- Sabes exactamente por qué la historia divergió (ej: usaste amend o rebase).\n"
         "Si trabajas en equipo, ¡puedes borrar el trabajo de otros!",
         "main"),
        ("4", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ],
    
    "branch_menu": [
        ("1", 
         "✨ **Crear Rama**\n\n"
         "- `git branch <nombre>`: Crea la rama pero no te cambia a ella.\n"
         "- `git checkout -b <nombre>`: Crea la rama y te cambia a ella automáticamente (Recomendado).", 
         "main"),
        ("2", 
         "twisted_rightwards_arrows **Cambiar Rama**\n\n"
         "- `git checkout <nombre>` (Clásico)\n"
         "- `git switch <nombre>` (Moderno, desde Git 2.23)", 
         "main"),
        ("3", 
         "📜 **Listar Ramas**\n\n"
         "- `git branch`: Ramas locales.\n"
         "- `git branch -a`: Locales y remotas.\n"
         "- `git branch -v`: Muestra el último commit de cada rama.", 
         "main"),
        ("4", 
         "🔥 **Borrar Rama**\n\n"
         "- `git branch -d <nombre>`: Borra si ya fue fusionada (seguro).\n"
         "- `git branch -D <nombre>`: Fuerza el borrado (cuidado, pierdes cambios no fusionados).", 
         "main"),
        ("5", "🔙 Volviendo...", "main"),
        ("menu", "🔙 Volviendo...", "main")
    ]
}

DEFAULT_RESPONSE = (
    "❓ **Comando no reconocido**\n\n"
    "Intenta usar palabras clave del menú principal:\n"
    "- `status`, `log`, `diff`, `commit`\n"
    "- `branch`, `push`, `conflict`\n\n"
    "O escribe **'ayuda'** para ver todas las opciones."
)
