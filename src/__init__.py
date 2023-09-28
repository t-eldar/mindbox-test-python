import schemas
from pyspark.sql import SparkSession

def get_product_with_categories():
  spark = SparkSession.builder.appName('mindbox-test-task').getOrCreate()
  p_df = spark.read\
    .option('multiline','true')\
    .schema(schemas.PRODUCT_SCHEMA)\
    .json('../data/products.json')
  c_df = spark.read\
    .option('multiline','true')\
    .schema(schemas.CATEGORY_SCHEMA)\
    .json('../data/categories.json')
  p_c_df = spark.read\
    .option('multiline','true')\
    .schema(schemas.PRODUCT_CATEGORY_SCHEMA)\
    .json('../data/products_categories.json')

  result_df = p_df.join(p_c_df, p_df.id == p_c_df.product_id, 'left')\
    .join(c_df, p_c_df.category_id == c_df.id, 'left')\
    .select(p_df.name.alias('ProductName'), c_df.name.alias('CategoryName'))
  
  return result_df



