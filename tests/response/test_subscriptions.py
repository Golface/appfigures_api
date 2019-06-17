from tests.data.response import Response
from appfigures_api.response.subscriptions import SubscriptionsGroupBy


class TestSubscriptions(object):

    def test_get_with_group_by(self):
        json = Response.get_subscriptions_json_with_two_group_by()
        response_group_by = SubscriptionsGroupBy(json, ['date', 'product'])

        print(response_group_by)

        assert 6 == len(response_group_by)

        for element in response_group_by:
            assert hasattr(element, 'active_subscriptions')
            assert hasattr(element, 'actual_revenue')
            assert hasattr(element, 'activations')
            assert hasattr(element, 'cancellations')
            assert hasattr(element, 'mrr')
            assert hasattr(element, 'churn')
            assert hasattr(element, 'gross_revenue')
            assert hasattr(element, 'gross_mrr')
            assert hasattr(element, 'first_year_subscribers')
            assert hasattr(element, 'non_first_year_subscribers')
            assert hasattr(element, 'active_trials')
            assert hasattr(element, 'new_trials')
            assert hasattr(element, 'cancelled_trials')
            assert hasattr(element, 'transitions_in')
            assert hasattr(element, 'transitions_out')
            assert hasattr(element, 'cancelled_subscriptions')
            assert hasattr(element, 'new_subscriptions')
            assert hasattr(element, 'trial_conversions')
            assert hasattr(element, 'reactivations')
            assert hasattr(element, 'renewals')
            assert hasattr(element, 'active_grace')
            assert hasattr(element, 'active_grace')
            assert hasattr(element, 'new_grace')
            assert hasattr(element, 'grace_drop_off')
            assert hasattr(element, 'grace_recovery')
            assert hasattr(element, 'new_trial_grace')
            assert hasattr(element, 'trial_grace_drop_off')
            assert hasattr(element, 'trial_grace_recovery')
            assert hasattr(element, 'date')
            assert hasattr(element, 'product_id')
            assert hasattr(element, 'iso')
            assert hasattr(element, 'country')
            assert hasattr(element, 'storefront')
            assert hasattr(element, 'store')
