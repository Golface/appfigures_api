from abc import ABCMeta
import base64


class BaseAPIClient(object, metaclass=ABCMeta):
    def __init__(self, base_url, requests):
        self._base_url = base_url
        self._requests = requests
        self._session = None
        self._params = {}
        self._client_key = ''
        self._personal_access_token = ''

    def set_client_key(self, client_key):
        self._client_key = client_key

    def set_credential(self, personal_access_token):
        self._personal_access_token = personal_access_token

    def set_params(self, params):
        self._params = params

    def _prepare_request(self):
        if self._session is not None:
            return

        headers = {
            'Authorization': 'Bearer {}'.format(self._personal_access_token)
        }

        self._session = self._requests.Session()
        self._session.headers.update(headers)
