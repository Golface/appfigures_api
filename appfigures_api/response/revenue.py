from .base import AppFiguresObject
from .base import AppFiguresGroupBy


class RevenueGroupBy(AppFiguresGroupBy):
    def __init__(self, json, group_by):
        super(RevenueGroupBy, self).__init__(json, group_by)

    def _transform(self, data):
        return RevenueObject.from_json(data)


class RevenueObject(AppFiguresObject):

    def _load(self, json):
        self.sales = json.get('json')
        self.iaps = json.get('iaps')
        self.ads = json.get('ads')
        self.edu = json.get('edu')
        self.returns = json.get('returns')
        self.total = json.get('total')
        self.gross_sales = json.get('gross_sales')
        self.gross_iap = json.get('gross_iap')
        self.gross_edu = json.get('gross_edu')
        self.gross_returns = json.get('gross_returns')
        self.date = json.get('date', None)
        self.product_id = json.get('product_id', None)
        self.iso = json.get('iso', None)
        self.country = json.get('country', None)
        self.storefront = json.get('storefront', None)
        self.store = json.get('store', None)
