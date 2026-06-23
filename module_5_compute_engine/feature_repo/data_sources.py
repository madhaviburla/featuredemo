from feast import FileSource
from feast.types import Int64, Float32

# driver_stats = SparkSource(
#     name="driver_stats_source",
#     path="../data/driver_stats_lat_lon.parquet",
#     timestamp_field="event_timestamp",
#     created_timestamp_column="created",
#     description="A table describing the stats of a driver based on hourly logs",
#     owner="test2@gmail.com",
# )


drivers_stat_source = FileSource(
    path="../data/customer_features.csv",
    timestamp_field="event_timestamp",
)
