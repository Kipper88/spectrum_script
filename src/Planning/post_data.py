from aiohttp import ClientSession
from const import urlApiPlanning

class PlanningPost:
    def __init__(self):
        self.urlApiPlanning = urlApiPlanning
        
    async def post_data(self, data):
        async with ClientSession() as sess:
            resp = await sess.post(url=self.urlApiPlanning,
                                  json=data,
                                  ssl=False
                                  )
            data = await resp.json()
            return data
            
            