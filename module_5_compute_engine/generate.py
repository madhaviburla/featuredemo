import pandas as pd
from datetime import datetime

df = pd.DataFrame({
     "customer_id": [101, 102, 103],
     "total_orders": [15, 3, 8],
     "days_since_last_purchase": [61, 10, 48],
     "last_90d_orders_count": [1, 8, 2],
     "avg_order_value": [42000.0, 8500.0, 3000.0],
     "support_ticket_count": [3, 1, 4],
     "login_count_last_30d": [2, 15, 1],
     "coupon_usage_rate": [0.15, 0.60, 0.20],
     "event_timestamp": [
         datetime.utcnow(),
         datetime.utcnow(),
         datetime.utcnow()
     ]
})

def segment_customer(x):
    if x >= 10:
        return "Premium"
    elif x >= 5:
        return "Regular"
    else:
        return "Low"
def predict_churn(days_since_last_purchase, last_90d_orders_count, login_count_last_30d):
    if (
         days_since_last_purchase > 45
         and last_90d_orders_count < 2
         and login_count_last_30d < 3
    ):
         return "High Churn Risk"
    return "Low/Medium Churn Risk"

df["customer_segment"] = df["total_orders"].apply(segment_customer)
df["churn_prediction"] = df.apply(
     lambda row: predict_churn(
         row["days_since_last_purchase"],
         row["last_90d_orders_count"],
         row["login_count_last_30d"]
          
     ),
     axis=1
)
print(df)

df.to_csv("module_5_compute_engine/data/customer_features.csv", index=False)

print("customer_features.csv ganerated successfully")
