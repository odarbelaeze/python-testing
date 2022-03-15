import requests


class BillingError(Exception):
    """
    Error interacting with the billing API.
    """

    pass


class Billing:
    """
    Talks to the external billing service.
    """

    def list_accounts(self):
        result = requests.get("https://api.mysite.com/billing/accounts")
        if not result.ok:
            raise BillingError("Failed to talk to the billing API")
        return result.json()
