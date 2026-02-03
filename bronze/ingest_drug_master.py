from utils.spark_session import get_spark_session
from utils.constants import RAW_PATH, BRONZE_PATH

spark = get_spark_session("bronze_drug_master")

df = spark.read.option("header", True).csv(f"{RAW_PATH}/drug_master.csv")

df.write.format("delta") \
    .mode("append") \
    .save(f"{BRONZE_PATH}/drug_master")
