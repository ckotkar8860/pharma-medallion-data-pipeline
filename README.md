## Pharma Medallion Data Pipeline

This project demonstrates a Medallion Architecture (Bronze, Silver, Gold)
data pipeline for a pharma analytics use case using PySpark and Databricks.

### Data Sources
- Patients
- Prescriptions
- Drug Master

### Architecture
- Bronze: Raw CSV ingestion into Delta tables
- Silver: Data cleaning and standardization
- Gold: Aggregated analytics for drug usage

### Tech Stack
- PySpark
- Databricks
- Delta Lake

### Output
Gold layer provides drug usage summary by category for analytics teams.
