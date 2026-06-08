from datetime import timedelta

from feast import (
    BatchFeatureView,
    Field,
)
import pyspark
from feast.types import String, Float32, Int64

from data_sources import *
from entities import *


def transform_feature(inputs: pyspark.sql.DataFrame):
    transformed_df = inputs.withColumn(
        "high_value_order",
            when(col("O_TOTALPRICE") >5000, 1).otherwise(0)
        ).withColumn(
            "order_completed",
            when(col("O_ORDERSTATUS") =="F", 1).otherwise(0)
        )
    print("transformation applied successfully")
    
     transformed_df.show(5)    
    return transformed_df


bfv = BatchFeatureView(
    name="order_stats",
    description="Hourly features",
    entities=[customer],
    schema=[
        Field(name="O_TOTALPRICE", dtype=Float32),
        Field(name="O_ORDERSTATUS", dtype=String),
        Field(name="O_high_value_order", dtype=Int64),
        Field(name="O_order_completed", dtype=Int64),
    ],
    udf=transform_feature,
    online=True,
    source=drivers_stat_source,
    tags={"production": "True"},
    owner="test2@gmail.com",
)
