from feast import Entity, BatchFeatureView, Field, FileSource
from feast.types import String, Float32, Int64

#from data_sources import drivers_stat_source
#from entities import customer
customer = Entity(name="customer_id", join_keys=["customer_id"])
drivers_stat_source = FileSource(
    path=".data/customer_features.csv",
    timestamp_field="event_timestamp",
    file_format="csv",
)

order_stats = BatchFeatureView(
    name="order_stats",
    entities=[customer],
    schema=[
        Field(name="O_TOTALPRICE", dtype=Float32),
        Field(name="O_ORDERSTATUS", dtype=String),
        Field(name="high_order_value", dtype=Int64),
        Field(name="order_completed", dtype=Int64),
    ],
    online=True,
    source=drivers_stat_source,
)
customer_segmentation = BatchFeatureView(
    name="customer_segmentation",
    entities=[customer],
    schema=[
        Field(name="total_orders", dtype=Float32),
        Field(name="customer_segment", dtype=String),
    ],
    online=True,
    source=drivers_stat_source,
)


cust0mer_churn = BatchFeatureView(
    name="customer_churn",
    entities=[customer],
    schema=[
        Field(name="days_since_last_purchase", dtype=Int64),
        Field(name="last_90d_order_count", dtype=Int64),
        Field(name="avg_order_value", dtype=Float32),
        Field(name="support_ticket_count", dtype=Int64),
        Field(name="login_count_last_30d", dtype=Int64),
        Field(name="cupon_usage_rate", dtype=Float32),
       
    ],
    online=True,
    source=drivers_stat_source,
)
