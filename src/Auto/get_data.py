from aiohttp import ClientSession
from const import *

class AutoGet:
    def __init__(self):
        self.URL_FOR_POST_DATA_TO_SPECTRUM = URL_FOR_POST_DATA_TO_SPECTRUM.format(type_request_auto)
        self.URL_FOR_GET_DATA_FROM_SPECTRUM = URL_FOR_GET_DATA_FROM_SPECTRUM
        
    async def post_spectrum(self, GRZ: str):
        async with ClientSession() as sess:
            headers = {
                "Accept": "application/json",
                "Authorization": "AR-REST dXNlcl9pbnRlZ3JhdGlvbkBidGdfc3BlZGl0aW9uOjE3Mjc5NjI0NTU6OTk5OTk5OTk5OldINDBwTlpNUzljVGtLUkNhbDgzOUE9PQ=="
            }
            params = {
                "queryType": "GRZ",
                "query": f"{GRZ}"
            }

            resp = await sess.post(
                url=self.URL_FOR_POST_DATA_TO_SPECTRUM,
                headers=headers,
                json=params)
            data = await resp.json()
            
            return data.get('data', [{}])[0].get('uid', {})
        
    async def get_spectrum(self, uid: str):
        url = self.URL_FOR_GET_DATA_FROM_SPECTRUM + f'/{uid}'
        async with ClientSession() as sess:
            headers = {
                "Accept": "application/json",
                "Authorization": "AR-REST dXNlcl9pbnRlZ3JhdGlvbkBidGdfc3BlZGl0aW9uOjE3Mjc5NjI0NTU6OTk5OTk5OTk5OldINDBwTlpNUzljVGtLUkNhbDgzOUE9PQ=="
            }
            params = {
                "_content": "true",
                "_detailed": "true"
            }
            resp = await sess.get(url=url,
                                headers=headers,
                                params=params)
            data = await resp.json()

            return data