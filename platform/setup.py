import os
import json
from schemas.create_schemas import create_schemas
from spark_session import get_spark

def load_config():
    env_path = os.getenv("SCHEMA_CONFIG_PATH")

    if env_path:
        return env_path

    try:
        with open("../configs/local_configs.json", "r") as f:
            config = json.load(f)
            return config["schema_config_path"]
    except Exception:
        raise ValueError(
            "No configuration found. Set SCHEMA_CONFIG_PATH or provide configs/local_config.json"
        )


def run_setup(spark):
    print("Starting platform setup...")

    config_path = load_config()

    print(f"Using config file: {config_path}")

    create_schemas(spark, config_path)

    print("Platform setup completed successfully.")


if __name__ == "__main__":
    run_setup(spark=get_spark())