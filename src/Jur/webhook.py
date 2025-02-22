from aiohttp import ClientSession
import json

from settings.cfgRukWebhook import fieldJur
from const import urlRuk, apiKeyRuk, usernameRuk, passRuk

async def readJsonFileJur():
    with open('temp/idsJur.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonJur(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsJur.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return None
    
    

class RukJurWebhook:
    def __init__(self):
        self.urlRuk = urlRuk
        self.apiKey = apiKeyRuk
        self.usernameRuk = usernameRuk
        self.passRuk = passRuk
        
    async def webhookJur(self):  
        params = {
            'key': self.apiKey,  # API ключ  
            'username': self.usernameRuk,                                   # Имя пользователя
            'password': self.passRuk,                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldJur['Jur'], 
            'select_fields': f"{fieldJur['inn']}",
            #'filter': {
            #    '159': datetime.now().strftime('%Y-%m-%d')
            #}
        }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  params=params,
                                  ssl=False
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFileJur()
        
        if await checkJsonJur(js, data['id']):
            return {fieldJur['inn']: data[fieldJur['inn']], 'id': data['id']}
