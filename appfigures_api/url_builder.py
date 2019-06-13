

class UrlBuilder:

    def __init__(self):
        self._base_url = ''
        self._url = ''

    def set_base_url(self, base_url):
        self._base_url = base_url
        return self

    def set_url(self, sub_url):
        self._url = '{}{}'.format(self._base_url, sub_url)
        return self

    def get_url(self):
        return self._url
