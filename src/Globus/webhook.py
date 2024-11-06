import json
from aiohttp import ClientSession

from const import apiKeyRuk, urlRuk
from settings.cfgRukWebhook import fieldGlobus

async def readJsonFileJur():
    with open('temp/idsGlobus.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonJur(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsGlobus.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return None

class RukGlobusWebhook:
    def __init__(self):
        self.urlRuk = urlRuk
        self.apiKey = apiKeyRuk
        
    async def webhook(self):
        params = {
            'key': self.apiKey,  # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldGlobus['Globus'], 
            'select_fields': f"\
                            {fieldGlobus['declarant_tin']},\
                            {fieldGlobus['start']},\
                            {fieldGlobus['finish']},\
                            {fieldGlobus['direction']}"
        }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  json=params
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFileJur()
        
        if await checkJsonJur(js, data['id']):
            return {fieldGlobus['declarant_tin']: data[fieldGlobus['declarant_tin']], 
                    fieldGlobus['start']: data[fieldGlobus['start']],
                    fieldGlobus['finish']: data[fieldGlobus['finish']],
                    fieldGlobus['direction']: data[fieldGlobus['direction']],
                    'id': data['id']}