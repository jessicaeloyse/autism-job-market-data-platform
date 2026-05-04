import yaml

def create_schemas(spark, config_path: str):
    """
    Create schemas in Databricks using a YAML configuration file.

    Args:
        spark: SparkSession
        config_path (str): Path to the YAML config file
    """

    # Carrega o YAML
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    print(config)

    schemas = config.get("schemas", [])

    for schema in schemas:
        name = schema["name"]
        comment = schema.get("comment", "")

        # Evita quebra de SQL por aspas
        comment = comment.replace("'", " ").strip()

        print(f"Creating schema: {name}")

        spark.sql(
            f"""
            CREATE SCHEMA IF NOT EXISTS autism_data_platform.{name}
            COMMENT '{comment}'
        """
        )

    print("All schemas created successfully.")


