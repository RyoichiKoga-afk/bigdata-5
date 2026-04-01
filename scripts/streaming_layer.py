import os
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STREAM_PATH = os.path.join(BASE_DIR, "stream_data")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "serving", "stream")
CHECKPOINT_PATH = os.path.join(BASE_DIR, "logs", "stream_checkpoint")

os.makedirs(STREAM_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(CHECKPOINT_PATH, exist_ok=True)

schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("city", StringType(), True),
    StructField("timestamp", StringType(), True)
])

spark = SparkSession.builder \
    .appName("StreamingPipeline") \
    .master("local[*]") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

stream_df = spark.readStream \
    .schema(schema) \
    .option("maxFilesPerTrigger", 1) \
    .json(STREAM_PATH)

query = stream_df.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", OUTPUT_PATH) \
    .option("checkpointLocation", CHECKPOINT_PATH) \
    .trigger(processingTime="5 seconds") \
    .start()

print("Spark streaming berjalan...")
print("Membaca dari:", STREAM_PATH)
print("Menyimpan ke:", OUTPUT_PATH)

query.awaitTermination()