
Readme by Hari Thapliyal

# NYC Parking Violation 

## Dataset Introduction
The NYC Department of Finance collects data on every parking ticket issued in NYC (~10M per year!)
There are four files, covering Aug 2013-June 2017. The files are roughly organized by fiscal year (July 1 - June 30) with the exception of the initial dataset.
- [Original Data Source](https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2024/pvqr-7yc4/about_data)
- [Kaggle Dataset](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets)

## Questions Explored

1. **Basic Data Overview:**
   - What is the total number of records in the dataset?
   - Are there any missing or null values in any of the columns?
   - What is the data type of each column, and are there any inconsistencies?

2. **Date Analysis:**
   - What is the range of ticket issue dates (earliest and latest)?
   - Are there any trends in ticket issuance over time (e.g., seasonal patterns, specific months with higher issuance)?
   - How many tickets were issued on weekends vs. weekdays?

3. **Violation Analysis:**
   - What are the most common violation codes, and how frequently do they occur?
   - Are there specific violation codes associated with certain vehicle makes or body types?
   - Is there any relationship between violation code and time of issuance (e.g., certain violations happen at specific times)?

4. **Vehicle Analysis:**
   - What are the most common vehicle makes and body types?
   - Are certain vehicle makes associated with a higher number of violations?
   - What is the distribution of ticket issuance across different registration states?

5. **Geographical Analysis:**
   - What is the distribution of tickets across different violation precincts and issuer precincts?
   - Are there specific areas (precincts) where violations are more concentrated?
   - Is there a geographic pattern in ticket issuance (e.g., certain areas are ticketed more often)?

6. **Violation Time:**
   - What are the most common times for violations to occur?
   - Are there particular hours or time periods where violations are more frequent?
   - Can violation times be linked to traffic patterns or specific events?

7. **Duplication & Uniqueness:**
   - Are there any duplicate entries in the dataset based on Summons Number or Plate ID?
   - Are there any cases where the same Plate ID has multiple violations on the same day?

8. **Violation Trends:**
   - How has the number of parking tickets issued changed over time (e.g., by year or month)?
   - Is there any noticeable change in violation patterns for specific vehicle makes or precincts over time?

9. **Correlations and Patterns:**
   - Are there any correlations between violation codes and vehicle body types or makes?
   - Are violations more common in specific precincts or certain time windows?

## Technology Used.
Since this is is bigdataset therefore, it is not possible to do analysis using pandas. So we used PySpark.

### What is RDD?
**[PySpark and RDD Reference Code](https://github.com/dasarpai/DAI-Projects/blob/main/Travel%2BLogistic/Bigdata-pySpark-NYC-Parking/Reference)**

RDDs are a special data type, tailor-made for Apache Spark. Indeed, the first boost of performance in Apache Spark came from the innovative nature of the RDD structure. An RDD can be considered as a distributed set of elements.

Traditional systems such as MapReduce, though distributed in nature, lack ways to utilise the main memory of a cluster’s resources. This makes them inappropriate for a certain type of computations - those that reuse the intermediate results during computation. RDDs have entered the industry and neatly filled in the gap that MapReduce has.

RDDs are data structures that are designed to effectively process big data. Following are the main properties of RDDs:

- Distributed collection of data
- Fault tolerance
- Parallel operations
- Ability to use varied data sources

### RDD Persistence
RDD persistence helps you to save the frequently-used RDDs or the output for future uses. By storing the intermediate RDDs or output in the cluster, you prevent the repeated task of evaluating the same results again and again. This helps in the efficient management of time and resources available.

There are two ways to persist RDDs in Spark:

- cache( )
- persist( )

### Important PySpark Syntex
```
!pip install pyspark
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("ml") \
    .getOrCreate()
	

df = spark.read.csv("/common_folder/heart.csv",header=True)
df.createOrReplaceTempView("dfTable")
df2=spark.sql("SELECT age  FROM dfTable")
df3=df2.withColumn("age2", df2["age"].cast("Int"))

from pyspark.ml.feature import Bucketizer
bucketizer = Bucketizer(splits=[29, 40, 50, 60, 70, 80], inputCol="age2", outputCol="buckets")
bucketed = bucketizer.transform(df3)
bucketed.groupBy("buckets").count().show()
bucketed.show()
bucketed.sort(bucketed.age2.asc()).collect()
df_heart = spark.read.csv("/common_folder/Advertising.csv",header=True)

sampled_data = df_heart2.select(numeric_features).sample(False, 0.8).toPandas()

df_home = spark.read.json("/common_folder/amazon_reviews_graded/reviews_Home_and_Kitchen_5.json")
df_home.show()

df_home.createOrReplaceTempView("dfHome") 
spark.sql("SELECT count( distinct asin) FROM dfHome").show()


spark.sql("SELECT count( distinct reviewerID) FROM dfHome").show()
review_length= spark.sql('SELECT helpful, overall, reviewText, reviewTime, summary, asin, LENGTH(reviewText) AS reviewLength FROM dfHome')
review_length.sort( review_length.reviewLength.desc()).show()

```