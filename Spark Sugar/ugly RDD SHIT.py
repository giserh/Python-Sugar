from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import LongType, TimestampType, StructType, StructField
from datetime import datetime
import ast

sqlContext = SQLContext(sc)
spark = SparkSession(sc)

rdd1 = sc.textFile("/data/static/sales_ignored_orders/20170117204900/part-00000.gz")
rdd1 = rdd1.union(sc.textFile("/data/static/sales_ignored_orders/20170117204900/part-00001.gz"))
rdd1 = rdd1.union(sc.textFile("/data/static/sales_ignored_orders/20170117204900/part-00002.gz"))
rdd1 = rdd1.union(sc.textFile("/data/static/sales_ignored_orders/20170117204900/part-00003.gz"))

rdd = rdd1.map(lambda x: ast.literal_eval(x))\
		 .map(lambda x: x.items())\
		 .map(lambda y: [y[0][1], datetime.strptime(y[1][1][:19], '%Y-%m-%dT%H:%M:%S')])

schema = StructType([StructField("order_id", LongType()), 
					 StructField("stop_threshold", TimestampType())]) 

df = rdd.toDF(schema)