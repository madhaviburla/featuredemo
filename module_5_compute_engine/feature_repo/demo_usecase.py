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

print("high valude customer feature")

print(df.to_string(index=False))

df,to_csv("customer_feature.csv", index=False)

print("customer_feature.csv generated successfully")
