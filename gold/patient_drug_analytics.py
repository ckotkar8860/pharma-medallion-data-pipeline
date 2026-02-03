from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("gold_patient_drug").getOrCreate()

patients = spark.read.format("delta").load("/mnt/delta/silver/patients")
prescriptions = spark.read.format("delta").load("/mnt/delta/silver/prescriptions")
drugs = spark.read.format("delta").load("/mnt/delta/silver/drug_master")

final_df = (
    prescriptions
    .join(patients, "patient_id")
    .join(drugs, "drug_id")
    .groupBy("drug_name", "category")
    .agg(sum("quantity").alias("total_quantity"))
)

final_df.write.format("delta") \
  .mode("overwrite") \
  .save("/mnt/delta/gold/drug_usage_summary")
