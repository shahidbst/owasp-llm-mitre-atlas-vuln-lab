MITRE_PROFILES = {
    "AML_T0024_002": {
        "base_function": "def predict(input_data):\n    return model.generate(input_data)\n",
        "mutations": [
            "no_auth",
            "no_rate_limit",
            "debug_mode",
            "hardcoded_secret",
            "unbounded_loop",
            "no_timeout",
            "no_logging",
            "missing_validation",
            "exposed_internal",
            "bypass_flag"
        ]
    }
}
