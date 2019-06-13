import json


class Response(object):

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
