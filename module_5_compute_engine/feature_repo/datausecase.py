from feast import FeatureStore

store = FeatureStore(repo_path=".")

#entity data
entity_rows = [
    {"customer_id": 1},
    {"customer_id": 2},
    {"customer_id": 3}
]
data = store.get_historical_features(
    entity_df=entity_rows,
    features=[
        "customer_features:high_value_order",
        "customer_features:order_completed",
        "customer_features:total_orders",
    ],
).to_df()

print("feature output:")
pritn(data)
 
