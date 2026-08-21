
df_silver = spark.read.parquet("abfss://retail@aakretail.dfs.core.windows.net/silver/")

from pyspark.sql import functions as F

df_daily_revenue = (
    df_silver.groupBy("event_date")
    .agg(F.sum("amount").alias("daily_revenue"), F.count("*").alias("total_purchases"))
)

df_daily_revenue.write.mode("overwrite").parquet("abfss://retail@aakretail.dfs.core.windows.net/gold/")

df_daily_revenue.show()
