import json
from aiohttp import ClientSession

from const import URL_FOR_POST_DATA_TO_SPECTRUM, URL_FOR_GET_DATA_FROM_SPECTRUM, type_request_passport

async def test(last_name, first_name, patronymic, birth, passport, passport_date, inn):
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
    headers = {
                "Accept": "application/json",
                "Authorization": "AR-REST dXNlcl9pbnRlZ3JhdGlvbkBidGdfc3BlZGl0aW9uOjE3Mjc5NjI0NTU6OTk5OTk5OTk5OldINDBwTlpNUzljVGtLUkNhbDgzOUE9PQ=="
            }
    async with ClientSession() as sess:
        resp = await sess.post(url=URL_FOR_POST_DATA_TO_SPECTRUM.format("report_check_passport_test@btg_spedition"),
                               json=params,
                               headers=headers)
        js = await resp.json()
        print(js)
        return(js['data'][0]['uid'])
            

async def get_spectrum(uid: str):
        url = URL_FOR_GET_DATA_FROM_SPECTRUM + f'/{uid}'
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

            with open('json.json', 'w') as f:
                json.dump(data, f, indent=4)
        
import asyncio

#uid = asyncio.run(test("Сафин", "Денис", "Петрович", "24.01.1994", "1914 955060", "", "781143108237"))
asyncio.run(get_spectrum('report_check_passport_test_fa18c1156fce37299c06002b52eba46b@btg_spedition'))