from aiohttp import ClientSession
from const import *

class PhysGet:
    def __init__(self):
        self.URL_FOR_POST_DATA_TO_SPECTRUM = URL_FOR_POST_DATA_TO_SPECTRUM.format(type_request_passport)
        self.URL_FOR_REFRESH_DATA_FROM_SPECTRUM = URL_FOR_REFRESH_DATA_FROM_SPECTRUM
        self.URL_FOR_GET_DATA_FROM_SPECTRUM = URL_FOR_GET_DATA_FROM_SPECTRUM
        
    async def post_spectrum(self,
                            last_name: str,
                            first_name: str,
                            patronymic: str,
                            birth: str,
                            passport: str,
                            passport_date: str,
                            inn: str
    ):
        async with ClientSession() as sess:
            headers = {
                "Accept": "application/json",
                "Authorization": "AR-REST dXNlcl9pbnRlZ3JhdGlvbkBidGdfc3BlZGl0aW9uOjE3Mjc5NjI0NTU6OTk5OTk5OTk5OldINDBwTlpNUzljVGtLUkNhbDgzOUE9PQ=="
            }
            params = {
                "queryType": "MULTIPART",
                "query": " ",
                "data": {
                    "last_name": last_name,
                    "first_name": first_name,
                    "patronymic": patronymic,
                    "birth": birth,
                    "passport": passport,
                    "passport_date": passport_date,
                    "inn": inn#,
                    #    "region": [
                    #   {
                    #        "codes": ["78"],
                    #        "fullName": "Санкт-Петербург"
                    #    }
                    #    ]

                }
            }

            resp = await sess.post(
                url=self.URL_FOR_POST_DATA_TO_SPECTRUM,
                headers=headers,
                json=params)
            data = await resp.json()
            
            uid = data.get('data', [{}])[0].get('uid', {})
            
            params['data']['settings'] = {}
            params['data']['settings']['FORCE'] = "true"
            
            resp = await sess.post(
                url=self.URL_FOR_REFRESH_DATA_FROM_SPECTRUM.format(uid),
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