import requests


class BillingError(Exception):
    """
    Error interacting with the billing API.
    """

    pass


class BillingAuthError(BillingError):
    """
    Error tokenenticating to the billing API.
    """


class Billing:
    """
    Talks to the external billing service.
    """

    def __init__(self, token=None):
        self._token = token
        self._session = requests.Session()
        if self._token:
            self._session.headers.setdefault("Authorization", f"Bearer {self._token}")

    def list_accounts(self):
        response = self._session.get("https://api.mysite.com/billing/accounts")
        if response.status_code == 403:
            raise BillingAuthError("Failed to tokenenticate to the billing API")
        if not response.ok:
            raise BillingError("Failed to talk to the billing API")
        return response.json()
