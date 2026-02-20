"""
OWASP LLM Top 10 & MITRE ATLAS Vulnerability Lab - Main Application
"""

from flask import Flask, request, jsonify
from llm_service import LLMService
import logging

app = Flask(__name__)
llm_service = LLMService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.route('/query', methods=['POST'])
def query():
    """Main LLM query endpoint"""
    try:
        data = request.get_json()
        prompt = data.get('prompt')
        vulnerability_type = data.get('type', 'safe')
        
        if not prompt:
            return jsonify({'error': 'prompt required'}), 400
        
        response = llm_service.process_query(prompt, vulnerability_type)
        return jsonify({'response': response}), 200
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/test-vulnerability/<vuln_type>', methods=['POST'])
def test_vulnerability(vuln_type):
    """Test specific vulnerability"""
    try:
        data = request.get_json()
        result = llm_service.test_vulnerability(vuln_type, data)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error testing vulnerability: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
