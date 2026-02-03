from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.appName("silver_patients").getOrCreate()

df = spark.read.format("delta").load("/mnt/delta/bronze/patients")

clean_df = (
    df.withColumn("dob", to_date(col("dob")))
      .dropDuplicates(["patient_id"])
)

clean_df.write.format("delta") \
  .mode("overwrite") \
  .save("/mnt/delta/silver/patients")
