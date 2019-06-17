from appfigures_api.revenue import Revenue
from .data.response import Response
import requests


class TestRevenue(object):

    def test_get_with_group_by(self, requests_mock):
        json = Response.get_revenue_json_with_four_group_by()
        requests_mock.register_uri('GET', 'https://test.appfigures.io/reports/revenue?group_by=date,product,country,store&start_date=2019-05-12&end_date=2019-05-13', request_headers={
            'X-Client-Key': 'abc1234567890Abc',
            'Authorization': 'Basic aGFsbzpoaWlp'
        }, complete_qs=True, json=json)

        base_url = 'https://test.appfigures.io'
        revenue_api = Revenue(base_url, requests)
        revenue_api.set_client_key('abc1234567890Abc')
        revenue_api.set_credential('halo', 'hiii')
        revenue_api.set_params({
            'group_by': ['date', 'product', 'country', 'store'],
            'start_date': '2019-05-12',
            'end_date': '2019-05-13'
        })
        result = revenue_api.get_with_group_by()

        assert 7 == len(result)
