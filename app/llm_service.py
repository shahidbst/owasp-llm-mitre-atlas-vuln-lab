"""
LLM Service Module - Handles LLM operations and vulnerability testing
"""

import openai
import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class LLMService:
    """Service for interacting with LLM models"""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """Initialize LLM service"""
        self.model = model
        self.max_tokens = 500
        self.temperature = 0.7
    
    def process_query(self, prompt: str, vulnerability_type: str = 'safe') -> str:
        """
        Process a query through the LLM
        
        Args:
            prompt: User input prompt
            vulnerability_type: Type of vulnerability to test
        
        Returns:
            LLM response
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling LLM: {str(e)}")
            raise
    
    def test_vulnerability(self, vuln_type: str, params: Dict[str, Any]) -> Dict:
        """
        Test specific vulnerability
        
        Args:
            vuln_type: Type of vulnerability to test
            params: Parameters for vulnerability test
        
        Returns:
            Test result
        """
        # Import vulnerable modules
        from vulnerable import prompt_injection, insecure_output
        
        handlers = {
            'prompt_injection': prompt_injection.test_prompt_injection,
            'insecure_output': insecure_output.test_insecure_output,
        }
        
        handler = handlers.get(vuln_type)
        if handler:
            return handler(params)
        else:
            return {'error': f'Unknown vulnerability type: {vuln_type}'}
