import sys
from pathlib import Path

# Agregar el directorio raíz del proyecto al path para permitir imports absolutos
# cuando se ejecuta directamente desde backend/
if __name__ == '__main__':
    # Resuelve la ruta absoluta al directorio raíz del proyecto
    project_root = Path(__file__).resolve().parent.parent
    sys.path.append(str(project_root))

from flask import Flask
from flask_cors import CORS
from backend.api.routes import api_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilitar CORS para permitir peticiones desde el frontend
    
    # Registrar Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return "<h1>🤖 El servidor del Asistente Git está funcionando!</h1><p>Abre <code>frontend/index.html</code> en tu navegador para usar el chat.</p>"
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("Servidor del Asistente Git corriendo en http://localhost:5000")
    app.run(debug=True, port=5000)
