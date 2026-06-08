from feast import BatchFeatureView, Field
from feast.types import String, Float32

bfv = BatchFeatureView(
    name="order_stats",
    schema=[
        Field(name="O_TOTALPRICE", dtype=Float32),
        Field(name="O_ORDERSTATUS", dtype=String),
    ],
    online=True,
)
