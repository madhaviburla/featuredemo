from feast import BatchFeatureView, Field
from feast.types import String, Float32

from data_sources import drivers_stat_source
from entities import customer

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
customer_segmentation_bfv = BatchFeatureView(
    name="customer_segmentation",
    entities=[customer],
    schema=[
        Field(name="O_TOTALPRICE", dtype=Float32),
        Field(name="customer_segment", dtype=String),
    ],
    online=True,
    source=drivers_stat_source,
)
