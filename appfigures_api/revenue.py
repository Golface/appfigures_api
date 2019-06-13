from appfigures_api.base import BaseAPIClient
from .response.revenue import RevenueGroupBy


class Revenue(BaseAPIClient):

    def get_with_group_by(self):
        self._prepare_request()
        r = self._session.get('{}{}'.format(self._base_url, '/reports/revenue'), params=self._params)

        if not r.ok:
            r.raise_for_status()

        json = r.json()
        response_group_by = RevenueGroupBy.from_json(json, self._params['group_by'])
        return response_group_by
