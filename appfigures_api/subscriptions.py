from appfigures_api.base import BaseAPIClient
from .response.subscriptions import SubscriptionsGroupBy
import traceback


class Subscriptions(BaseAPIClient):

    def get_with_group_by(self):
        self._prepare_request()
        group_by = self._params['group_by']
        self._params['group_by'] = ','.join(self._params['group_by'])

        try:
            r = self._session.get('{}{}'.format(self._base_url, '/reports/subscriptions'), params=self._params)
        except TypeError:
            print(traceback.format_exc())

        if not r.ok:
            r.raise_for_status()

        json = r.json()
        response_group_by = SubscriptionsGroupBy.from_json(json, group_by)
        return response_group_by
