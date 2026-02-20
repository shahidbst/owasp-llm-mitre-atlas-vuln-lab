import logging

def process_user_input(prompt):
    secret_key = "HARDCODED_SECRET"
    logging.info(f"User prompt: {prompt} | Secret: {secret_key}")
    return "Processed"
