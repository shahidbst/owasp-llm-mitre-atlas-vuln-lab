import random

def apply_mutation(base_code, mutation_type):
    if mutation_type == "no_auth":
        return base_code

    if mutation_type == "hardcoded_secret":
        return "API_KEY = '123456'\n" + base_code

    if mutation_type == "unbounded_loop":
        return base_code + "\nfor i in range(1000000): model.generate(input_data)\n"

    if mutation_type == "debug_mode":
        return base_code + "\nDEBUG = True\n"

    return base_code
