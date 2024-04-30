from .base import AppFiguresObject
from .base import AppFiguresGroupBy


class SubscriptionsGroupBy(AppFiguresGroupBy):
    def __init__(self, json, group_by):
        super(SubscriptionsGroupBy, self).__init__(json, group_by)

    def _transform(self, data):
        return SubscriptionObject.from_json(data)


class SubscriptionObject(AppFiguresObject):

    def _load(self, json):
        self.active_subscriptions = json.get('active_subscriptions')
        self.actual_revenue = json.get('actual_revenue')
        self.activations = json.get('activations')
        self.cancellations = json.get('cancellations')
        self.mrr = json.get('mrr')
        self.churn = json.get('churn')
        self.gross_revenue = json.get('gross_revenue')
        self.gross_mrr = json.get('gross_mrr')
        self.first_year_subscribers = json.get('first_year_subscribers')
        self.non_first_year_subscribers = json.get('non_first_year_subscribers')
        self.active_trials = json.get('active_trials')
        self.new_trials = json.get('new_trials')
        self.cancelled_trials = json.get('cancelled_trials')
        self.transitions_in = json.get('transitions_in')
        self.transitions_out = json.get('transitions_out')
        self.cancelled_subscriptions = json.get('cancelled_subscriptions')
        self.new_subscriptions = json.get('new_subscriptions')
        self.trial_conversions = json.get('trial_conversions')
        self.reactivations = json.get('reactivations')
        self.renewals = json.get('renewals')
        self.active_grace = json.get('active_grace')
        self.new_grace = json.get('new_grace')
        self.grace_drop_off = json.get('grace_drop_off')
        self.grace_recovery = json.get('grace_recovery')
        self.new_trial_grace = json.get('new_trial_grace')
        self.trial_grace_drop_off = json.get('trial_grace_drop_off')
        self.trial_grace_recovery = json.get('trial_grace_recovery')
        self.date = json.get('date', None)
        self.product_id = json.get('product_id', None)
        self.iso = json.get('iso', None)
        self.country = json.get('country', None)
        self.storefront = json.get('storefront', None)
        self.store = json.get('store', None)
