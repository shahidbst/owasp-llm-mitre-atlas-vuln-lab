def auto_execute_generated_code(code_from_llm):
    # Blind trust in LLM output
    exec(code_from_llm)
