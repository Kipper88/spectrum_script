import json
from aiohttp import ClientSession

from const import apiKeyRuk, urlRuk
from settings.cfgRukWebhook import fieldPhys

async def readJsonFilePhys():
    with open('temp/idsPhys.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonPhys(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsPhys.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return None
class RukPhysWebhook:
    def __init__(self):
        self.urlRuk = urlRuk
        self.apiKey = apiKeyRuk
        
    async def webhook(self):
        params = {
            'key': self.apiKey,  # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldPhys['Phys'], 
            'select_fields': f"\
                            {fieldPhys['last_name']},\
                            {fieldPhys['first_name']},\
                            {fieldPhys['patronymic']},\
                            {fieldPhys['birth']},\
                            {fieldPhys['passport']},\
                            {fieldPhys['passport_date']},\
                            {fieldPhys['inn']}"
            #'filter': {
            #    '159': datetime.now().strftime('%Y-%m-%d')
            #}
        }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  json=params
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFilePhys()
        
        if await checkJsonPhys(js, data['id']):
            return {fieldPhys['last_name']: data[fieldPhys['last_name']], 
                    fieldPhys['first_name']: data[fieldPhys['first_name']],
                    fieldPhys['patronymic']: data[fieldPhys['patronymic']],
                    fieldPhys['birth']: data[fieldPhys['birth']],
                    fieldPhys['passport']: data[fieldPhys['passport']],
                    fieldPhys['passport_date']: data[fieldPhys['passport_date']],
                    fieldPhys['inn']: data[fieldPhys['inn']],
                    'id': data['id']}