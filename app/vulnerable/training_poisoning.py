"""
LLM03 - Training Data Poisoning
Demonstrates training data poisoning vulnerabilities
"""

import logging
import hashlib

logger = logging.getLogger(__name__)


def test_training_poisoning(params: dict) -> dict:
    """
    Test training data poisoning vulnerability
    
    Args:
        params: Test parameters including training data
    
    Returns:
        Test result
    """
    training_data = params.get('data', [])
    
    # VULNERABLE: No data validation or integrity checks
    poisoned_samples = detect_poisoned_samples(training_data)
    
    return {
        'vulnerability': 'Training Data Poisoning',
        'total_samples': len(training_data),
        'poisoned_count': len(poisoned_samples),
        'risk_level': 'CRITICAL' if poisoned_samples else 'LOW'
    }


def detect_poisoned_samples(data: list) -> list:
    """Detect potentially poisoned training data"""
    poisoned = []
    
    for idx, sample in enumerate(data):
        # Check for suspicious patterns
        if isinstance(sample, dict):
            text = sample.get('text', '').lower()
            
            # Look for injection patterns
            if text.count('ignore instructions') > 0:
                poisoned.append(idx)
            elif text.count('confidential') > 3:
                poisoned.append(idx)
        
    return poisoned


def validate_training_data(data: list) -> dict:
    """
    Validate training data integrity
    
    Args:
        data: Training data to validate
    
    Returns:
        Validation result
    """
    validation_result = {
        'valid': True,
        'errors': [],
        'warnings': []
    }
    
    for idx, sample in enumerate(data):
        # Check structure
        if not isinstance(sample, dict):
            validation_result['valid'] = False
            validation_result['errors'].append(f'Sample {idx}: Invalid structure')
        
        # Check required fields
        if 'text' not in sample or 'label' not in sample:
            validation_result['valid'] = False
            validation_result['errors'].append(f'Sample {idx}: Missing required fields')
        
        # Check for suspicious content
        if isinstance(sample.get('text'), str) and len(sample['text']) > 10000:
            validation_result['warnings'].append(f'Sample {idx}: Unusually large')
    
    return validation_result
