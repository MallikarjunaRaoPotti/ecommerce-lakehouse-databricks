# Databricks notebook source
# DBTITLE 1,Cell 1: Monthly revenue summary
# MAGIC %sql
# MAGIC SELECT 
# MAGIC year,
# MAGIC month_name,
# MAGIC SUM(unit_price * quantity) AS revenue
# MAGIC FROM ecommerce.gold.fact_transactions_denorm
# MAGIC GROUP BY year, month_name
# MAGIC ORDER BY year, month_name;

# COMMAND ----------

df = spark.sql("""
SELECT 
date_trunc('month', transaction_ts) AS month,
SUM(unit_price * quantity) AS revenue
FROM ecommerce.gold.fact_transactions_denorm
GROUP BY month
ORDER BY month
""")

pdf = df.toPandas()

# COMMAND ----------

# MAGIC %pip install prophet

# COMMAND ----------

from prophet import Prophet

pdf.columns = ["ds","y"]

model = Prophet()
model.fit(pdf)

# COMMAND ----------

future = model.make_future_dataframe(periods=6, freq="M")

forecast = model.predict(future)

forecast[['ds','yhat']].tail()

# COMMAND ----------

spark.createDataFrame(
forecast[['ds','yhat']]
).write.mode("overwrite").saveAsTable(
"ecommerce.gold.revenue_forecast"
)