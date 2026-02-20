"""
LLM01 - Prompt Injection
Demonstrates prompt injection vulnerabilities
"""

import logging

logger = logging.getLogger(__name__)


def test_prompt_injection(params: dict) -> dict:
    """
    Test prompt injection vulnerability
    
    Args:
        params: Test parameters including 'prompt'
    
    Returns:
        Test result
    """
    prompt = params.get('prompt', '')
    
    # VULNERABLE: Direct concatenation with user input
    system_prompt = "You are a helpful assistant. Only answer questions about math."
    full_prompt = f"{system_prompt}\n\nUser: {prompt}"
    
    injection_indicators = [
        'ignore',
        'forget',
        'disregard',
        'override',
        'system prompt',
        'instruction',
        'jailbreak'
    ]
    
    detected = any(indicator.lower() in prompt.lower() for indicator in injection_indicators)
    
    return {
        'vulnerability': 'Prompt Injection',
        'prompt': prompt,
        'detected': detected,
        'risk_level': 'HIGH' if detected else 'LOW'
    }


def safe_prompt_injection(user_input: str) -> str:
    """
    Safe prompt handling with proper input validation
    
    Args:
        user_input: User provided input
    
    Returns:
        Processed output
    """
    # Remove potentially dangerous characters and patterns
    sanitized = user_input.replace('\n', ' ').replace('\r', '')
    
    # Use input validation
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000]
    
    return sanitized


def generate_response(system_prompt, user_input):
    # Vulnerable: user input overrides system instructions
    full_prompt = f"{system_prompt}\nUser: {user_input}"
    return call_llm(full_prompt)

def call_llm(prompt):
    return f"LLM Output: {prompt}"



