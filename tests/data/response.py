import json


class Response(object):

    @staticmethod
    def get_revenue_json_with_two_group_by():
        return json.loads("""
            {
                "2019-05-12": {
                    "39936627333": {
                        "sales": "0.00",
                        "iap": "277.24",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "277.24",
                        "gross_sales": "0.00",
                        "gross_iap": "408.92",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "408.92",
                        "date": "2019-05-12",
                        "product_id": 39936627333
                    },
                    "40189303832": {
                        "sales": "0.00",
                        "iap": "100.10",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "100.10",
                        "gross_sales": "0.00",
                        "gross_iap": "143.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "143.00",
                        "date": "2019-05-12",
                        "product_id": 40189303832
                    },
                    "280442837017": {
                        "sales": "0.00",
                        "iap": "0.00",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "0.00",
                        "gross_sales": "0.00",
                        "gross_iap": "0.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "0.00",
                        "date": "2019-05-12",
                        "product_id": 280442837017
                    },
                    "280442837472": {
                        "sales": "0.00",
                        "iap": "0.00",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "0.00",
                        "gross_sales": "0.00",
                        "gross_iap": "0.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "0.00",
                        "date": "2019-05-12",
                        "product_id": 280442837472
                    }
                },
                "2019-05-13": {
                    "39936627333": {
                        "sales": "0.00",
                        "iap": "1356.00",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "1356.00",
                        "gross_sales": "0.00",
                        "gross_iap": "1780.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "1780.00",
                        "date": "2019-05-13",
                        "product_id": 39936627333
                    },
                    "40189303832": {
                        "sales": "0.00",
                        "iap": "200.20",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "200.20",
                        "gross_sales": "0.00",
                        "gross_iap": "286.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "286.00",
                        "date": "2019-05-13",
                        "product_id": 40189303832
                    },
                    "280442837017": {
                        "sales": "0.00",
                        "iap": "0.00",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "0.00",
                        "gross_sales": "0.00",
                        "gross_iap": "0.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "0.00",
                        "date": "2019-05-13",
                        "product_id": 280442837017
                    },
                    "280442837472": {
                        "sales": "0.00",
                        "iap": "0.00",
                        "returns": "0.00",
                        "edu": "0.00",
                        "ads": "0.00",
                        "total": "0.00",
                        "gross_sales": "0.00",
                        "gross_iap": "0.00",
                        "gross_edu": "0.00",
                        "gross_returns": "0.00",
                        "gross_total": "0.00",
                        "date": "2019-05-13",
                        "product_id": 280442837472
                    }
                }
            }
        """)

    @staticmethod
    def get_revenue_json_with_four_group_by():
        return json.loads("""
            {
                "2019-05-12": {
                    "39936627333": {
                        "JP": {
                            "apple:ios": {
                                "sales": "0.00",
                                "iap": "118.24",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "118.24",
                                "gross_sales": "0.00",
                                "gross_iap": "168.92",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "168.92",
                                "date": "2019-05-12",
                                "product_id": 39936627333,
                                "iso": "JP",
                                "country": "Japan",
                                "storefront": "apple:ios",
                                "store": "apple"
                            }
                        },
                        "TW": {
                            "apple:ios": {
                                "sales": "0.00",
                                "iap": "159.00",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "159.00",
                                "gross_sales": "0.00",
                                "gross_iap": "240.00",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "240.00",
                                "date": "2019-05-12",
                                "product_id": 39936627333,
                                "iso": "TW",
                                "country": "Taiwan",
                                "storefront": "apple:ios",
                                "store": "apple"
                            }
                        }
                    },
                    "40189303832": {
                        "JP": {
                            "google_play": {
                                "sales": "0.00",
                                "iap": "0.00",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "0.00",
                                "gross_sales": "0.00",
                                "gross_iap": "0.00",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "0.00",
                                "date": "2019-05-12",
                                "product_id": 40189303832,
                                "iso": "JP",
                                "country": "Japan",
                                "storefront": "google_play",
                                "store": "google_play"
                            }
                        },
                        "TW": {
                            "google_play": {
                                "sales": "0.00",
                                "iap": "100.10",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "100.10",
                                "gross_sales": "0.00",
                                "gross_iap": "143.00",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "143.00",
                                "date": "2019-05-12",
                                "product_id": 40189303832,
                                "iso": "TW",
                                "country": "Taiwan",
                                "storefront": "google_play",
                                "store": "google_play"
                            }
                        }
                    }
                },
                "2019-05-13": {
                    "39936627333": {
                        "JP": {
                            "apple:ios": {
                                "sales": "0.00",
                                "iap": "0.00",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "0.00",
                                "gross_sales": "0.00",
                                "gross_iap": "0.00",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "0.00",
                                "date": "2019-05-13",
                                "product_id": 39936627333,
                                "iso": "JP",
                                "country": "Japan",
                                "storefront": "apple:ios",
                                "store": "apple"
                            }
                        },
                        "TW": {
                            "apple:ios": {
                                "sales": "0.00",
                                "iap": "1356.00",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "1356.00",
                                "gross_sales": "0.00",
                                "gross_iap": "1780.00",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "1780.00",
                                "date": "2019-05-13",
                                "product_id": 39936627333,
                                "iso": "TW",
                                "country": "Taiwan",
                                "storefront": "apple:ios",
                                "store": "apple"
                            }
                        }
                    },
                    "40189303832": {
                        "TW": {
                            "google_play": {
                                "sales": "0.00",
                                "iap": "200.20",
                                "returns": "0.00",
                                "edu": "0.00",
                                "ads": "0.00",
                                "total": "200.20",
                                "gross_sales": "0.00",
                                "gross_iap": "286.00",
                                "gross_edu": "0.00",
                                "gross_returns": "0.00",
                                "gross_total": "286.00",
                                "date": "2019-05-13",
                                "product_id": 40189303832,
                                "iso": "TW",
                                "country": "Taiwan",
                                "storefront": "google_play",
                                "store": "google_play"
                            }
                        }
                    }
                }
            }
            """)

    @staticmethod
    def get_subscriptions_json_with_two_group_by():
        return json.loads("""
            {
              "2019-05-12": {
                "281311469596": {
                  "active_subscriptions": 17,
                  "active_free_trials": 0,
                  "new_subscriptions": 0,
                  "cancelled_subscriptions": 0,
                  "new_trials": 0,
                  "trial_conversion_rate": "0.00",
                  "mrr": "705.31",
                  "actual_revenue": "0.00",
                  "renewals": 0,
                  "first_year_subscribers": 0,
                  "non_first_year_subscribers": 0,
                  "reactivations": 0,
                  "transitions_out": 0,
                  "trial_cancellations": 0,
                  "transitions_in": 0,
                  "activations": 0,
                  "cancellations": 0,
                  "trial_conversions": 0,
                  "churn": "0.0000",
                  "gross_revenue": "0.00",
                  "gross_mrr": "1007.59",
                  "active_grace": 0,
                  "new_grace": 0,
                  "grace_drop_off": 0,
                  "grace_recovery": 0,
                  "new_trial_grace": 0,
                  "trial_grace_drop_off": 0,
                  "trial_grace_recovery": 0,
                  "active_trials": 0,
                  "date": "2019-05-12",
                  "product_id": 281311469596
                },
                "281311469599": {
                  "active_subscriptions": 8,
                  "active_free_trials": 0,
                  "new_subscriptions": 0,
                  "cancelled_subscriptions": 0,
                  "new_trials": 0,
                  "trial_conversion_rate": "0.00",
                  "mrr": "356.83",
                  "actual_revenue": "0.00",
                  "renewals": 0,
                  "first_year_subscribers": 0,
                  "non_first_year_subscribers": 0,
                  "reactivations": 0,
                  "transitions_out": 0,
                  "trial_cancellations": 0,
                  "transitions_in": 0,
                  "activations": 0,
                  "cancellations": 0,
                  "trial_conversions": 0,
                  "churn": "0.0000",
                  "gross_revenue": "0.00",
                  "gross_mrr": "509.75",
                  "active_grace": 0,
                  "new_grace": 0,
                  "grace_drop_off": 0,
                  "grace_recovery": 0,
                  "new_trial_grace": 0,
                  "trial_grace_drop_off": 0,
                  "trial_grace_recovery": 0,
                  "active_trials": 0,
                  "date": "2019-05-12",
                  "product_id": 281311469599
                }
              },
              "2019-05-13": {
                "281013177794": {
                  "active_subscriptions": 68,
                  "active_free_trials": 0,
                  "new_subscriptions": 1,
                  "cancelled_subscriptions": 1,
                  "new_trials": 0,
                  "trial_conversion_rate": "0.00",
                  "mrr": "7397.56",
                  "actual_revenue": "319.00",
                  "renewals": 2,
                  "first_year_subscribers": 40,
                  "non_first_year_subscribers": 28,
                  "reactivations": 0,
                  "transitions_out": 0,
                  "trial_cancellations": 0,
                  "transitions_in": 0,
                  "activations": 1,
                  "cancellations": 1,
                  "trial_conversions": 0,
                  "churn": "0.0147",
                  "gross_revenue": "450.00",
                  "gross_mrr": "9740.99",
                  "active_grace": 0,
                  "new_grace": 0,
                  "grace_drop_off": 0,
                  "grace_recovery": 0,
                  "new_trial_grace": 0,
                  "trial_grace_drop_off": 0,
                  "trial_grace_recovery": 0,
                  "active_trials": 0,
                  "date": "2019-05-13",
                  "product_id": 281013177794
                },
                "281013177795": {
                  "active_subscriptions": 42,
                  "active_free_trials": 0,
                  "new_subscriptions": 0,
                  "cancelled_subscriptions": 0,
                  "new_trials": 0,
                  "trial_conversion_rate": "0.00",
                  "mrr": "2222.77",
                  "actual_revenue": "0.00",
                  "renewals": 0,
                  "first_year_subscribers": 13,
                  "non_first_year_subscribers": 29,
                  "reactivations": 0,
                  "transitions_out": 0,
                  "trial_cancellations": 0,
                  "transitions_in": 0,
                  "activations": 0,
                  "cancellations": 0,
                  "trial_conversions": 0,
                  "churn": "0.0000",
                  "gross_revenue": "0.00",
                  "gross_mrr": "2767.10",
                  "active_grace": 0,
                  "new_grace": 0,
                  "grace_drop_off": 0,
                  "grace_recovery": 0,
                  "new_trial_grace": 0,
                  "trial_grace_drop_off": 0,
                  "trial_grace_recovery": 0,
                  "active_trials": 0,
                  "date": "2019-05-13",
                  "product_id": 281013177795
                },
                "281311469349": {
                  "active_subscriptions": 24,
                  "active_free_trials": 0,
                  "new_subscriptions": 0,
                  "cancelled_subscriptions": 0,
                  "new_trials": 0,
                  "trial_conversion_rate": "0.00",
                  "mrr": "1475.75",
                  "actual_revenue": "0.00",
                  "renewals": 0,
                  "first_year_subscribers": 9,
                  "non_first_year_subscribers": 15,
                  "reactivations": 0,
                  "transitions_out": 0,
                  "trial_cancellations": 0,
                  "transitions_in": 0,
                  "activations": 0,
                  "cancellations": 0,
                  "trial_conversions": 0,
                  "churn": "0.0000",
                  "gross_revenue": "0.00",
                  "gross_mrr": "1859.89",
                  "active_grace": 1,
                  "new_grace": 0,
                  "grace_drop_off": 0,
                  "grace_recovery": 0,
                  "new_trial_grace": 0,
                  "trial_grace_drop_off": 0,
                  "trial_grace_recovery": 0,
                  "active_trials": 0,
                  "date": "2019-05-13",
                  "product_id": 281311469349
                },
                "281311469350": {
                  "active_subscriptions": 235,
                  "active_free_trials": 0,
                  "new_subscriptions": 0,
                  "cancelled_subscriptions": 0,
                  "new_trials": 0,
                  "trial_conversion_rate": "0.00",
                  "mrr": "15629.21",
                  "actual_revenue": "878.00",
                  "renewals": 1,
                  "first_year_subscribers": 111,
                  "non_first_year_subscribers": 124,
                  "reactivations": 0,
                  "transitions_out": 0,
                  "trial_cancellations": 0,
                  "transitions_in": 0,
                  "activations": 0,
                  "cancellations": 0,
                  "trial_conversions": 0,
                  "churn": "0.0000",
                  "gross_revenue": "1090.00",
                  "gross_mrr": "20062.58",
                  "active_grace": 1,
                  "new_grace": 0,
                  "grace_drop_off": 0,
                  "grace_recovery": 0,
                  "new_trial_grace": 0,
                  "trial_grace_drop_off": 0,
                  "trial_grace_recovery": 0,
                  "active_trials": 0,
                  "date": "2019-05-13",
                  "product_id": 281311469350
                }
              }
            }
        """)
