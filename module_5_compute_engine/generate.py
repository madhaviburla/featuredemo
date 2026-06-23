import pandas as pd

df = pd.DataFrame({
     "customer_id": [101, 102, 103],
     "total_orders": [15, 3, 8],
})

def segment_customer(x):
    if x >= 10:
        return "Premium"
    elif x >= 5:
        return "Regular"
    else:
        return "Low"

df["customer_segment"] = df["total_orders"].apply(segment_customer)

print(df)
