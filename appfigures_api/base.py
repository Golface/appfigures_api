from abc import ABCMeta
import base64


class BaseAPIClient(object, metaclass=ABCMeta):
    def __init__(self, base_url, requests):
        self._base_url = base_url
        self._requests = requests
        self._session = None
        self._params = {}
        self._client_key = ''
        self._username = ''
        self._password = ''

    def set_client_key(self, client_key):
        self._client_key = client_key

    def set_credential(self, username, password):
        self._username = username
        self._password = password

    def set_params(self, params):
        self._params = params

    def _prepare_request(self):
        if self._session is not None:
            return

        credential = '{}:{}'.format(self._username, self._password)
        headers = {
            'X-Client-Key': self._client_key,
            'Authorization': 'Basic {}'.format(base64.b64encode(credential))
        }

        self._session = self._requests.Session()
        self._session.headers.update(headers)
