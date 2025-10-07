# # try:
# from pyspark import SparkConf
# from pyspark.sql import SparkSession
# from pyspark.sql import DataFrame
# from IPython.display import display
# import pyspark.sql.functions as f
# import requests
# import pandas as pd
# import os

# # --------------------------
# # Configuração Spark
# # --------------------------

# conf = SparkConf()

# conf.setAppName("Sample write Delta table")

# # Conexão com o MinIO (S3 compatível)
# conf.set("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
# conf.set("spark.hadoop.fs.s3a.access.key", "minio")
# conf.set("spark.hadoop.fs.s3a.secret.key", "minio123")
# conf.set("spark.hadoop.fs.s3a.path.style.access", True)
# conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
# conf.set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")

# # Delta Lake
# conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
# conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

# # Hive Metastore (se você tiver o serviço metastore no seu docker-compose)
# conf.set("hive.metastore.uris", "thrift://metastore:9083")

# # # Define o FS padrão como local (evita conflitos)
# conf.set("spark.hadoop.fs.defaultFS", "file:///")

# # --------------------------
# # Cria a SparkSession
# # --------------------------
# spark = (
#     SparkSession.builder
#     .config(conf=conf)
#     # .master("spark://spark-master:7077") 
#     .enableHiveSupport()
#     .getOrCreate()
# )

# ## Display formato pandas.
# def _repr_html_(self):
#     pdf = self.limit(20).toPandas()
#     for col in pdf.select_dtypes(include="datetime64").columns:
#         pdf[col] = pdf[col].astype("datetime64[ns]")
#     return pdf._repr_html_()

# DataFrame._repr_html_ = _repr_html_

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

def create_spark_session() -> SparkSession:
    conf = SparkConf()

    conf.setAppName("Sample write Delta table")

    # Conexão com o MinIO (S3 compatível)
    conf.set("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
    conf.set("spark.hadoop.fs.s3a.access.key", "minio")
    conf.set("spark.hadoop.fs.s3a.secret.key", "minio123")
    conf.set("spark.hadoop.fs.s3a.path.style.access", True)
    conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    conf.set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")

    # Delta Lake
    conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    # Hive Metastore (se tiver)
    conf.set("hive.metastore.uris", "thrift://metastore:9083")

    # Define o FS padrão como local (evita conflitos)
    conf.set("spark.hadoop.fs.defaultFS", "file:///")

    spark = (
        SparkSession.builder
        .config(conf=conf)
        # .master("spark://spark-master:7077") # se quiser cluster remoto
        .enableHiveSupport()
        .getOrCreate()
    )

    # Exibir DataFrame no Jupyter no formato pandas bonitão
    def _repr_html_(self):
        pdf = self.limit(20).toPandas()
        for col in pdf.select_dtypes(include="datetime64").columns:
            pdf[col] = pdf[col].astype("datetime64[ns]")
        return pdf._repr_html_()

    DataFrame._repr_html_ = _repr_html_

    return spark
