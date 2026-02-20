"""
SQL Plugin - Demonstrates vulnerable database plugin
"""

import logging

logger = logging.getLogger(__name__)


class SQLPlugin:
    """SQL execution plugin for LLM"""
    
    def __init__(self, connection_string: str):
        """Initialize SQL plugin"""
        self.connection_string = connection_string
        self.connection = None
    
    def execute_query(self, query: str) -> dict:
        """
        Execute SQL query - VULNERABLE TO INJECTION
        
        Args:
            query: SQL query string
        
        Returns:
            Query results
        """
        try:
            # VULNERABLE: No input sanitization - SQL injection risk
            logger.warning(f"Executing query: {query}")
            # Simulated execution
            return {"status": "executed", "query": query}
        except Exception as e:
            logger.error(f"SQL execution error: {str(e)}")
            return {"error": str(e)}
    
    def validate_query(self, query: str) -> bool:
        """
        Validate SQL query before execution
        
        Args:
            query: SQL query to validate
        
        Returns:
            True if query is safe, False otherwise
        """
        dangerous_keywords = ['DROP', 'DELETE', 'TRUNCATE', 'ALTER']
        return not any(keyword in query.upper() for keyword in dangerous_keywords)
