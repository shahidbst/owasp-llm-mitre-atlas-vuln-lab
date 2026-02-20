"""
File Plugin - Demonstrates vulnerable file operations plugin
"""

import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class FilePlugin:
    """File operations plugin for LLM"""
    
    def __init__(self, base_path: str = '/tmp'):
        """Initialize file plugin"""
        self.base_path = base_path
    
    def read_file(self, file_path: str) -> dict:
        """
        Read file contents - VULNERABLE TO PATH TRAVERSAL
        
        Args:
            file_path: Path to file
        
        Returns:
            File contents
        """
        try:
            # VULNERABLE: No path validation - path traversal risk
            full_path = os.path.join(self.base_path, file_path)
            logger.warning(f"Reading file: {full_path}")
            
            with open(full_path, 'r') as f:
                content = f.read(10000)  # Limit read size
            
            return {"content": content, "path": full_path}
        except Exception as e:
            logger.error(f"File read error: {str(e)}")
            return {"error": str(e)}
    
    def write_file(self, file_path: str, content: str) -> dict:
        """
        Write file contents - VULNERABLE TO PATH TRAVERSAL
        
        Args:
            file_path: Path to file
            content: Content to write
        
        Returns:
            Operation result
        """
        try:
            # VULNERABLE: No path validation - path traversal risk
            full_path = os.path.join(self.base_path, file_path)
            logger.warning(f"Writing to file: {full_path}")
            
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            with open(full_path, 'w') as f:
                f.write(content)
            
            return {"status": "written", "path": full_path}
        except Exception as e:
            logger.error(f"File write error: {str(e)}")
            return {"error": str(e)}
    
    def validate_path(self, file_path: str) -> bool:
        """
        Validate file path for security
        
        Args:
            file_path: Path to validate
        
        Returns:
            True if path is safe
        """
        # Check for path traversal attempts
        try:
            full_path = os.path.join(self.base_path, file_path)
            real_path = os.path.realpath(full_path)
            base_real = os.path.realpath(self.base_path)
            return real_path.startswith(base_real)
        except:
            return False
