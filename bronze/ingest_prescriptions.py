from utils.spark_session import get_spark_session
from utils.constants import RAW_PATH, BRONZE_PATH

spark = get_spark_session("bronze_prescriptions")

df = spark.read.option("header", True).csv(f"{RAW_PATH}/prescriptions.csv")

df.write.format("delta") \
    .mode("append") \
    .save(f"{BRONZE_PATH}/prescriptions")
