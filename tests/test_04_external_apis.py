import pook
import pytest
from deepthought.services.billing import Billing, BillingError


@pytest.fixture(autouse=True)
def intercept():
    with pook.use():
        yield


def test_list_billing_accounts():
    billing = Billing()
    pook.get("https://api.mysite.com/billing/accounts").reply(200).json([])
    result = billing.list_accounts()
    assert result == []


def test_list_billing_accounts_with_existing_accounts():
    billing = Billing()
    expected = [{"id": 123412341234, "name": "Very legit account"}]
    pook.get("https://api.mysite.com/billing/accounts").reply(200).json(expected)
    result = billing.list_accounts()
    assert result == expected


def test_billing_raises_a_billing_exception_if_the_billing_service_is_down():
    billing = Billing()
    pook.get("https://api.mysite.com/billing/accounts").reply(500).json(
        {"message": "everything is fine"}
    )
    with pytest.raises(BillingError):
        billing.list_accounts()
