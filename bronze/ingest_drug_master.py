from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("bronze_patients").getOrCreate()

df = spark.read.option("header", True).csv("/mnt/data/raw/patients.csv")

df.write.format("delta") \
  .mode("append") \
  .save("/mnt/delta/bronze/patients")
