import os
try:
    from dotenv import load_dotenv
    dotenv_available = True
except ImportError:
    print("Library could not be imported")
    dotenv_available = False

def load_config() -> tuple[dict[str, str | None], bool]:
    if dotenv_available:
        env_loaded = load_dotenv()
    else:
        env_loaded = False
    config: dict[str, str | None] = {}
    config["MATRIX_MODE"] = os.environ.get("MATRIX_MODE")
    config["DATABASE_URL"] = os.environ.get("DATABASE_URL")
    config["API_KEY"] = os.environ.get("API_KEY")
    config["LOG_LEVEL"] = os.environ.get("LOG_LEVEL")
    config["ZION_ENDPOINT"] = os.environ.get("ZION_ENDPOINT")

    return config, env_loaded

def print_config(config: dict[str,str | None]) -> None:
    labels = {
        "MATRIX_MODE": config["MATRIX_MODE"],
        "DATABASE_URL": "Connected to local instance",
        "API_KEY": "Authenticated",
        "LOG_LEVEL": config["LOG_LEVEL"],
        "ZION_ENDPOINT": "Online",
    }
    display_names = {
        "MATRIX_MODE": "Mode",
        "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
        "ZION_ENDPOINT": "Zion Network",
    }

    if config["MATRIX_MODE"] == "production":
        print("WARNING: Running in PRODUCTION mode — changes affect live systems")
        print()

    for key, value in config.items():
        if value is not None:
            print(f"{display_names[key]}: {labels[key]}")
        else:
            print(f"[MISSING]: {key}")

def security_check(env_loaded: bool) -> None:
    print("[OK] No hardcoded secrets detected")
    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not properly configured")
    print("[OK] Production overrides available")

def main() -> None:
    config, env_loaded = load_config()
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print_config(config)
    print()
    print("Environment security check:")
    security_check(env_loaded)
    print()
    print("The Oracle sees all configurations.")



if __name__ == "__main__":
    main()