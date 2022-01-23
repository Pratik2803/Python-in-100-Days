import requests


class ExeApi:
    CONTENT_TYPE = 'application/json'

    def __init__(self, api_id: str, api_key: str, url: str, query: str):
        self.api_id = api_id
        self.api_key = api_key
        self.url = url
        self.query = query

    def req_header(self) -> dict:
        header = {
            'x-app-id': self.api_id,
            'x-app-key': self.api_key,
            'Content-Type': ExeApi.CONTENT_TYPE
        }

        return header

    def req_body(self) -> dict:
        body = {
            "query": self.query
        }

        return body

    def req_response(self) -> dict:
        response = requests.post(url=self.url, headers=self.req_header(), json=self.req_body())
        response.raise_for_status()

        return response.json()
