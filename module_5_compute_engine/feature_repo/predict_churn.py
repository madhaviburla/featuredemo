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
