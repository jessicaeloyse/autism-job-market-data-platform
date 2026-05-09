from pyspark.sql import SparkSession

def get_spark(app_name: str = "data-platform"):
    spark = SparkSession.getActiveSession()

    if spark:
        print("Using existing Spark session")
        return spark

    print("Creating new Spark session")

    return SparkSession.builder.appName(app_name).getOrCreate()