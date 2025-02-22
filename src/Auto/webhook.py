from aiohttp import ClientSession
from datetime import datetime
import json

from const import urlRuk, apiKeyRuk, usernameRuk, passRuk
from settings.cfgRukWebhook import fieldAuto

async def readJsonAuto():
    with open('temp/idsAuto.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonAuto(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsAuto.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return False

class RukAutoWebhook: 
    def __init__(self):
        ...
    
    async def webhookAuto(self):
        params = {
            'key': apiKeyRuk,  # API ключ  
            'username': usernameRuk,                                   # Имя пользователя
            'password': passRuk,                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldAuto['Auto'], 
            'select_fields': f"{fieldAuto['GRZ']}",
            #'filters': {
            #    '159': datetime.now().strftime('%Y-%m-%d')
            #}
            }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=urlRuk,
                                  json=params
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonAuto()
        if await checkJsonAuto(js, data['id']):
            return {fieldAuto['GRZ']: data[fieldAuto['GRZ']], 'id': data['id']}
        return None
