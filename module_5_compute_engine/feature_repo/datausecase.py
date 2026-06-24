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
        "customer_features:total_price",
        "customer_features:order_count",
        "customer_features:high_value_customer",
    ],
).to_df()

print("feature output:")
pritn(data)
 
