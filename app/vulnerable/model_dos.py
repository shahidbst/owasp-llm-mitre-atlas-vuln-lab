"""
LLM04 - Model Denial of Service (DoS)
Demonstrates model DoS vulnerabilities
"""

import logging
import time

logger = logging.getLogger(__name__)


class ModelDoSSimulator:
    """Simulate model DoS vulnerabilities"""
    
    def __init__(self):
        """Initialize DoS simulator"""
        self.request_log = {}
        self.token_usage = {}
    
    def test_dos_attack(self, user_id: str, tokens_requested: int) -> dict:
        """
        Test DoS vulnerability with excessive token requests
        
        Args:
            user_id: User identifier
            tokens_requested: Number of tokens requested
        
        Returns:
            Test result
        """
        # VULNERABLE: No rate limiting or token quota
        self.token_usage[user_id] = self.token_usage.get(user_id, 0) + tokens_requested
        
        return {
            'vulnerability': 'Model Denial of Service',
            'user_id': user_id,
            'tokens_requested': tokens_requested,
            'total_tokens': self.token_usage[user_id],
            'status': 'processed'
        }
    
    def check_dos_vulnerability(self, user_id: str) -> dict:
        """Check if user is performing DoS attack"""
        total_tokens = self.token_usage.get(user_id, 0)
        
        return {
            'total_tokens': total_tokens,
            'is_dos_attack': total_tokens > 100000,
            'risk_level': 'CRITICAL' if total_tokens > 100000 else 'LOW'
        }


def test_model_dos(params: dict) -> dict:
    """
    Test model DoS vulnerability
    
    Args:
        params: Test parameters
    
    Returns:
        Test result
    """
    simulator = ModelDoSSimulator()
    user_id = params.get('user_id', 'user1')
    request_count = params.get('requests', 100)
    tokens_per_request = params.get('tokens_per_request', 1000)
    
    for i in range(request_count):
        simulator.test_dos_attack(user_id, tokens_per_request)
    
    result = simulator.check_dos_vulnerability(user_id)
    result['vulnerability'] = 'Model DoS'
    
    return result

def process_prompt(prompt):
    # Vulnerable: no input length restriction
    heavy_operation = prompt * 1000000
    return len(heavy_operation)
