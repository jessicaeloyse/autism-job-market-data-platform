import logging
from pyspark.sql import SparkSession

class PlatformContext:
    def __init__(self, app_name: str = "autism-data-platform"):
        self.spark = self._init_spark(app_name)
        self.logger = self._init_logger(app_name)

    def _init_spark(self, app_name: str) -> SparkSession:
        spark = SparkSession.getActiveSession()
        if spark:
            return spark
        return SparkSession.builder.appName(app_name).getOrCreate()

    def _init_logger(self, app_name: str) -> logging.Logger:
        logger = logging.getLogger(app_name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger