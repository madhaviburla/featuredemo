from feast import Entity, BatchFeatureView, Field, FileSource
from feast.types import String, Float32, Int64
from fest.value_type import ValueType


#from data_sources import drivers_stat_source
#from entities import customer

customer = Entity(
    name="customer_features", 
    join_keys=["customer_id"],
    value_type=ValueType.INT64,
)
drivers_stat_source = FileSource(
    path=".data/customer_data.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
    
)

order_stats = BatchFeatureView(
    name="order_stats",
    entities=[customer],
    schema=[
        Field(name="O_TOTALPRICE", dtype=Float32),
        #Field(name="O_ORDERSTATUS", dtype=String),
        Field(name="high_order_value", dtype=Int64),
        #Field(name="order_completed", dtype=Int64),
        Field(name="order_count", dtype=Int=64),
    ],
    online=False,
    source=drivers_stat_source,
)
#customer_segmentation = BatchFeatureView(
 #   name="customer_segmentation",
  #  entities=[customer],
    #schema=[
     #   Field(name="total_orders", dtype=Float32),
       # Field(name="customer_segment", dtype=String),
   # ],
   # online=False,
    #source=drivers_stat_source,
#)


#cust0mer_churn = BatchFeatureView(
    #name="customer_churn",
    #entities=[customer],
    #schema=[
        #Field(name="days_since_last_purchase", dtype=Int64),
        #Field(name="last_90d_order_count", dtype=Int64),
        #Field(name="avg_order_value", dtype=Float32),
        #Field(name="support_ticket_count", dtype=Int64),
        #Field(name="login_count_last_30d", dtype=Int64),
        #Field(name="cupon_usage_rate", dtype=Float32),
       
    #],
    #online=False,
    #source=drivers_stat_source,
#)
