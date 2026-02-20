"""
LLM02 - Insecure Output Handling
Demonstrates insecure output handling vulnerabilities
"""

import logging
import re

logger = logging.getLogger(__name__)


def test_insecure_output(params: dict) -> dict:
    """
    Test insecure output handling
    
    Args:
        params: Test parameters
    
    Returns:
        Test result
    """
    output = params.get('output', '')
    target_system = params.get('target', 'web')
    
    # VULNERABLE: Direct output without encoding
    risks = detect_output_risks(output, target_system)
    
    return {
        'vulnerability': 'Insecure Output Handling',
        'output': output,
        'detected_risks': risks,
        'risk_level': 'HIGH' if risks else 'LOW'
    }


def detect_output_risks(output: str, target_system: str) -> list:
    """Detect potential risks in output"""
    risks = []
    
    # Check for code execution patterns
    code_patterns = [
        r'<script[^>]*>',
        r'javascript:',
        r'<iframe[^>]*>',
        r'onclick=',
        r'onerror='
    ]
    
    for pattern in code_patterns:
        if re.search(pattern, output, re.IGNORECASE):
            risks.append(f'Potential {target_system} injection detected')
    
    # Check for SQL patterns
    if any(keyword in output.upper() for keyword in ['DROP', 'INSERT', 'DELETE']):
        risks.append('Potential SQL injection detected')
    
    return risks


def sanitize_output(output: str, target_system: str = 'web') -> str:
    """
    Sanitize output for safe display
    
    Args:
        output: Raw output to sanitize
        target_system: Target system type
    
    Returns:
        Sanitized output
    """
    if target_system == 'web':
        # HTML escape
        replacements = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#x27;'
        }
        for old, new in replacements.items():
            output = output.replace(old, new)
    
    return output



from flask import Response

def render_output(model_output):
    # Vulnerable: no escaping
    return Response(f"<html>{model_output}</html>", mimetype="text/html")
