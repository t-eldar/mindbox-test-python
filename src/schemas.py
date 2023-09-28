from pyspark.sql.types import (
  StructType, 
  StructField,
  StringType,
  IntegerType
)

CATEGORY_SCHEMA = StructType([
  StructField('id', IntegerType(), False),
  StructField('name', StringType(), False)
])
PRODUCT_SCHEMA = StructType([
  StructField('id', IntegerType(), False),
  StructField('name', StringType(), False)
])
PRODUCT_CATEGORY_SCHEMA = StructType([
  StructField('product_id', IntegerType()),
  StructField('category_id', IntegerType())
])