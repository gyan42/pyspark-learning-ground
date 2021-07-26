# pyspark-learning-ground

PySpark refresh guide with examples and reference links for quick try outs!


## Spark Setup

```
My machine has following configuration...
- 6 cores with 12vCores
- 32GB RAM
```

Spark Standalone server:
```
cd /opt/softwares/spark-3.0.1-bin-hadoop3.2/

export PYSPARK_PYTHON=/opt/envs/ai4e/bin/python
export PYSPARK_DRIVER_PYTHON=/opt/envs/ai4e/bin/python

sbin/start-all.sh
sbin/stop-all.sh
```
Spark UI: [http://localhost:8080](http://localhost:8080)   
Spark Master URL : spark://IMCHLT276:7077


## Spark Session

```
spark = SparkSession.builder \
    .master("spark://IMCHLT276:7077") \
    .config("spark.sql.autoBroadcastJoinThreshold", -1) \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", "2") \
    .config("spark.cores.max", "6") \
    .config("spark.local.dir", "/opt/tmp/spark-temp/") \
    .appName("DataSkewness") \
    .getOrCreate()

```
