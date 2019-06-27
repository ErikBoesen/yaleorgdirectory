import requests


class Organization(dict):
    def __init__(self, raw):
        self.update(raw)
        self.update(self.__dict__)


class YaleOrgDirectory:
    API_TARGET = 'https://gw.its.yale.edu/soa-gateway/org/directory'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get(self, params: dict = {}):
        """
        Make a GET request to the API.

        :param params: dictionary of custom params to add to request.
        """
        params.update({
            'apikey': self.api_key,
            'type': 'json',
        })
        request = requests.get(self.API_TARGET, params=params)
        if request.ok:
            return request.json()
        else:
            # TODO: Can we be more helpful?
            raise Exception('API request failed. Data returned: ' + request.text)

    def organizations(self, tags=[]):
        params = {}
        if tags:
            if type(tags) == list:
                tags = ','.join(tags)
            params['tags'] = tags
        return [Organization(raw) for raw in self.get(params)]
