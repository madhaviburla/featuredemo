import pandas as pd

data = {
    "customer_id": [101, 102, 103],
    "O_TOTALPRICE": [7000, 2000, 9000],
    "O_ORDERSTATUS": ["F", "O", "F"],
}

df = pd.DataFrame(data)

df["high_value_order"] = df["O_TOTALPRICE"].apply(
    lambda x: 1 if x >5000 else 0
)

df["order_completed"] = df["O_ORDERSTATUS"].apply(
    lambda x:1 if x == "F" else 0
)

# segmentation features
df["total_orders"] = [15, 5, 20]
df["customer_segment"] = ["High", "Low", "High"]

# Churn Features
df["days_since_last_purchase"] = [5, 20, 2]
df["last_90d_order_count"] = [3, 1, 6]
df["avg_order_value"] = df["O_TOTALPRICE"]
df["support_ticket_count"] = [2, 1, 0]
df["login_count_last_30d"] = [10, 5, 18]
df["coupon_usage_rate"] = [0.30, 0.10, 0.45]

# Feast source timestamp
df["event_timestamp"] = "2024-06-01 10:00:00"

print("customer_feature.csv generated successfully")

print(df.to_string(index=False))

df.to_csv("customer_feature.csv", index=False)


