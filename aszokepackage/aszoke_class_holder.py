import requests


class AszokeClass():

    def __init__(self) -> None:
        pass

    def do_http_get(self, url) -> requests.Response:
        return requests.get(url)
