from feast import BatchFeatureView, Field
from feast.types import String, Float32
from data_source import *
from entities import *

bfv = BatchFeatureView(
    name="order_stats",
    entities=[customer],
    schema=[
        Field(name="O_TOTALPRICE", dtype=Float32),
        Field(name="O_ORDERSTATUS", dtype=String),
    ],
    online=True,
    source=drivers_stat_source,
)
