import json
from feast import FeatureStore


def classify_churn(days_since_last_purchase, last_90d_order_count, login_count_last_30d):
    if ( 
         days_since_last_purchase > 45
         and last_90d_order_count < 2
         and login_count_last_30d < 3
    ):
         return "High Churn Risk"
      return "Low/Medium Churn Risk"


def main():
    customer_id = 500

    store = FeatureStore(repo_path="feature repo")

    feature_vector = store.get_online_features(
        feature=[,
            "customers_features:days_since_last_purchase",
            "customers_features:last_90d_order_count",
            "customers_features:avg_order_value",
            "customers_features:support_ticket_count",
            "customers_features:login_count_last_30d",
            "customers_features:cupon_usage_rate",
      ],
      entity_rows=[{"custimer_id": customer_id}],
    ).to_dict()

   days_since_last_purchase = feature_vector ["days_since_last_purchase"][0]
   last_90d_order_count = feature_vector ["last_90d_order_count"][0]
   login_count_last_30d = feature_vector ["login_count_last_30d"][0]

  result = {
       "customers_id": customers_id,
        "days_since_last_purchase": days_since_last_purchase,
        "last_90d_order_count": avg_order_value,
        "feature_vector[avg_order_value]"[0],
        "support_ticket_count": feature_vector["support_ticket_count"][0],
        "login_count_last_30":  login_count_last_30d,
        "cupon_usage_rate": feature_vector["cupon_usage_rate"][0]
        "prediction": classify_churn(
            days_since_last_purchase,
            last_90d_order_count,
            login_count_last_30d,
       ),
  }
  
  print(json.dumps(result, indent=2, default=str))


if__name__ == "__main__":
   main()
