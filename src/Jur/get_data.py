from aiohttp import ClientSession
from const import *

class JurGet:
    def __init__(self):
        self.URL_FOR_POST_DATA_TO_SPECTRUM = URL_FOR_POST_DATA_TO_SPECTRUM.format(type_request_kontrAgent)
        self.URL_FOR_GET_DATA_FROM_SPECTRUM = URL_FOR_GET_DATA_FROM_SPECTRUM
        
    async def post_spectrum_jur_face(self, inn: str):
        async with ClientSession() as sess:
            headers = {
                "Accept": "application/json",
                "Authorization": api_key_spec
            }
            params = {
                "queryType": "MULTIPART",
                "query": " ",
                "data": {
                    "inn": inn
                }
            }
            resp = await sess.post(
                url=self.URL_FOR_POST_DATA_TO_SPECTRUM,
                headers=headers,
                json=params,
                ssl=False)
            data = await resp.json()
            
            return data.get('data', [{}])[0].get('uid', {})
        
    async def get_spectrum_jur_face(self, uid: str):
        url = self.URL_FOR_GET_DATA_FROM_SPECTRUM + f'/{uid}'
        async with ClientSession() as sess:
            headers = {
                "Accept": "application/json",
                "Authorization": api_key_spec
            }
            params = {
                "_content": "true",
                "_detailed": "true"
            }
            resp = await sess.get(url=url,
                                headers=headers,
                                params=params,
                                ssl=False)
            data = await resp.json()

            return data