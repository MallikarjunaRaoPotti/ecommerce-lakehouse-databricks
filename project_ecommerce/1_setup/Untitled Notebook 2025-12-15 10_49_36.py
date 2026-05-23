# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS ecommerce

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG ecommerce;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS ecommerce.bronze;
# MAGIC create schema if not exists ecommerce.silver;
# MAGIC create schema if not exists ecommerce.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC show databases from ecommerce;

# COMMAND ----------

