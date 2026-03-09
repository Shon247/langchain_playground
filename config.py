import os

# Load API keys from environment variables — never hardcode secrets here
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
            if "API" in key or "ID" in key:
                  os.environ[key] = value
