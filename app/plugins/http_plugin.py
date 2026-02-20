"""
HTTP Plugin - Demonstrates vulnerable HTTP request plugin
"""

import requests
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class HTTPPlugin:
    """HTTP request plugin for LLM"""
    
    def __init__(self, timeout: int = 30):
        """Initialize HTTP plugin"""
        self.timeout = timeout
        self.max_retries = 3
    
    def make_request(self, url: str, method: str = 'GET', headers: Dict = None, data: Any = None) -> Dict:
        """
        Make HTTP request - VULNERABLE TO SSRF
        
        Args:
            url: Target URL
            method: HTTP method
            headers: Request headers
            data: Request body
        
        Returns:
            Response data
        """
        try:
            # VULNERABLE: No URL validation - SSRF risk
            logger.warning(f"Making {method} request to: {url}")
            
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                timeout=self.timeout,
                allow_redirects=True
            )
            
            return {
                "status_code": response.status_code,
                "content": response.text[:500]  # Truncate large responses
            }
        except Exception as e:
            logger.error(f"HTTP request error: {str(e)}")
            return {"error": str(e)}
    
    def validate_url(self, url: str) -> bool:
        """
        Validate URL for security
        
        Args:
            url: URL to validate
        
        Returns:
            True if URL is valid and safe
        """
        blocked_schemes = ['file://', 'gopher://', 'data://']
        blocked_hosts = ['localhost', '127.0.0.1', '172.', '192.168.']
        
        return not any(url.startswith(scheme) for scheme in blocked_schemes) and \
               not any(host in url for host in blocked_hosts)
