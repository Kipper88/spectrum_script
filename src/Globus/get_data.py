from aiohttp import ClientSession
from const import *

class GlobusGet:
    def __init__(self):
        self.urlGlobus = urlGlobus
        self.apiKeyGlobus = apiKeyGlobus
        
    async def get_data(self,
                        declarant_tin: str,
                        start: str,
                        finish: str,
                        direction: str
    ):
        async with ClientSession() as sess:
            params = {
                "api-key": self.apiKeyGlobus,
                "method": "save",
                "period_start": start,
                "period_finish": finish,
                "search[direction]": direction,
                "search[declarant_tin]": declarant_tin,
                "fields_view[]": [
                    "country_departure",
                    "country_destination",
                    "incoterms",
                    "price_usd",
                    "sender_name",
                    "recipient_tin",
                    "recipient_name"
                ]
            }

            resp = await sess.post(
                url=self.urlGlobus,
                params=params,
                ssl=False)
            data = await resp.json()
            
            return data