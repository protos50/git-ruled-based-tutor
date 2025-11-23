from flask import Blueprint, request, jsonify
from backend.core.agent import GitAgent

api_bp = Blueprint('api', __name__)
agent = GitAgent()

@api_bp.route('/ask', methods=['POST'])
def ask_agent():
    """Endpoint principal del asistente.
    Ahora soporta parámetro opcional 'lang' ('es' | 'en').
    """
    try:
        data = request.get_json(silent=True) or {}
        question = data.get('question')
        if not question:
            return jsonify({'error': 'Falta el campo "question"'}), 400

        session_id = data.get('session_id', 'default')  # session
        lang = data.get('lang', 'es')
        if lang not in ('es', 'en'):
            lang = 'es'

        response = agent.get_response(question, session_id=session_id, lang=lang)

        return jsonify({
            'question': question,
            'response': response,
            'session_id': session_id,
            'lang': lang
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'agent': 'GitAssistant v1.0'})
