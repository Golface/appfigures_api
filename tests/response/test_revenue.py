from appfigures_api.response.revenue import RevenueGroupBy
from tests.data.response import Response


class TestRevenue(object):

    def test_init_with_multiple_group_by(self):
        json = Response.get_revenue_json_with_four_group_by()
        response_group_by = RevenueGroupBy(json, ['date', 'product', 'country', 'store'])

        print(response_group_by)

        assert 7 == len(response_group_by)

        for element in response_group_by:
            assert hasattr(element, 'sales')
            assert hasattr(element, 'iaps')
            assert hasattr(element, 'ads')
            assert hasattr(element, 'edu')
            assert hasattr(element, 'returns')
            assert hasattr(element, 'total')
            assert hasattr(element, 'gross_sales')
            assert hasattr(element, 'gross_iap')
            assert hasattr(element, 'gross_edu')
            assert hasattr(element, 'gross_returns')
            assert hasattr(element, 'date')
            assert hasattr(element, 'product_id')
            assert hasattr(element, 'iso')
            assert hasattr(element, 'country')
            assert hasattr(element, 'storefront')
            assert hasattr(element, 'store')
