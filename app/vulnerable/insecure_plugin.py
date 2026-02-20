def execute_query(user_input):
    # SQL injection
    sql = f"SELECT * FROM users WHERE name = '{user_input}'"
    return sql

def fetch_url(user_input):
    # SSRF vulnerability
    import requests
    return requests.get(user_input).text
