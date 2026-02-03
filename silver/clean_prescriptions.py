from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date

spark = SparkSession.builder.appName("silver_prescriptions").getOrCreate()

df = spark.read.format("delta").load("/mnt/delta/bronze/prescriptions")

df_clean = df.withColumn("prescription_date", to_date("prescription_date"))

df_clean.write.format("delta") \
  .mode("overwrite") \
  .save("/mnt/delta/silver/prescriptions")
