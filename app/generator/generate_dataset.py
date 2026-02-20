import os
from mitre_profiles import MITRE_PROFILES
from mutation_engine import apply_mutation

def generate_variants(mitre_id, count=100):
    profile = MITRE_PROFILES[mitre_id]
    base = profile["base_function"]
    mutations = profile["mutations"]

    os.makedirs(f"dataset/{mitre_id}", exist_ok=True)

    for i in range(count):
        mutation = mutations[i % len(mutations)]
        code = apply_mutation(base, mutation)

        with open(f"dataset/{mitre_id}/variant_{i+1}.py", "w") as f:
            f.write(code)

generate_variants("AML_T0024_002")
