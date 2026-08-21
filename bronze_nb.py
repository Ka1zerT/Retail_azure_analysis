from pyspark.sql.functions import col, to_date, lower

df_bronze = spark.read.parquet("abfss://retail@aakretail.dfs.core.windows.net/bronze/Ka1zerT/Retail_azure_analysis/refs/heads/main/retail_transactions_bronze.parquet")

df_bronze.show()
