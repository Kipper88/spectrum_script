from aiohttp import ClientSession
from const import *

class DriverGet:
    def __init__(self):
        self.URL_FOR_POST_DATA_TO_SPECTRUM = URL_FOR_POST_DATA_TO_SPECTRUM.format(type_request_dl)
        self.URL_FOR_GET_DATA_FROM_SPECTRUM = URL_FOR_GET_DATA_FROM_SPECTRUM
        
    async def post_spectrum(
        self,
        driver_license: str, 
        driver_license_date: str, 
        last_name: str, 
        first_name: str, 
        patronymic: str,
        birth: str
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
                    "driver_license": driver_license,  # номер лицензии ВУ
                    "driver_license_date": driver_license_date,    # дата выдачи лицензии ВУ
                    "last_name": last_name,    # фамилия
                    "first_name": first_name,  # имя
                    "patronymic": patronymic,  # отчество
                    "birth": birth             # дата рождения водителя
                }
            }

            resp = await sess.post(
                url=self.URL_FOR_POST_DATA_TO_SPECTRUM,
                headers=headers,
                json=params,
                ssl=False)
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
    
    """ async def post_spectrum_percent(self, last_name: str, first_name: str, patronymic: str, birth: str):
        async with ClientSession() as sess:
            headers = {
                "Accept": "application/json",
                "Authorization": "AR-REST dXNlcl9pbnRlZ3JhdGlvbkBidGdfc3BlZGl0aW9uOjE3Mjc5NjI0NTU6OTk5OTk5OTk5OldINDBwTlpNUzljVGtLUkNhbDgzOUE9PQ=="
            }
            params = {
                "queryType": "MULTIPART",
                "query": " ",
                "data": {
                    "last_name": last_name,    # фамилия
                    "first_name": first_name,  # имя
                    "patronymic": patronymic,  # отчество
                    "birth": birth             # дата рождения водителя
                }
            }

            resp = await sess.post(
                url=self.URL_FOR_POST_DATA_TO_SPECTRUM,
                headers=headers,
                json=params)
            data = await resp.json()
            
            return data.get('data', [{}])[0].get('uid', {})
        
    async def get_spectrum_percent(self, uid):
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

            return data """