import json
from aiohttp import ClientSession

from const import apiKeyRuk, urlRuk, usernameRuk, passRuk
from settings.cfgRukWebhook import fieldIP

async def readJsonFileJur():
    with open('temp/idsIP.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonJur(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsIP.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return None

class RukIPWebhook:
    def __init__(self):
        self.urlRuk = urlRuk
        self.apiKey = apiKeyRuk
        self.usernameRuk = usernameRuk
        self.passRuk = passRuk
        
    async def webhook(self):
        params = {
            'key': self.apiKey,  # API ключ  
            'username': self.usernameRuk,                                   # Имя пользователя
            'password': self.passRuk,                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldIP['IP'], 
            'select_fields': f"\
                            {fieldIP['last_name']},\
                            {fieldIP['first_name']},\
                            {fieldIP['patronymic']},\
                            {fieldIP['birth']},\
                            {fieldIP['passport']},\
                            {fieldIP['inn']}"
            #'filter': {
            #    '159': datetime.now().strftime('%Y-%m-%d')
            #}
        }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  json=params,
                                  ssl=False
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFileJur()
        
        if await checkJsonJur(js, data['id']):
            return {fieldIP['last_name']: data[fieldIP['last_name']], 
                    fieldIP['first_name']: data[fieldIP['first_name']],
                    fieldIP['patronymic']: data[fieldIP['patronymic']],
                    fieldIP['birth']: data[fieldIP['birth']],
                    fieldIP['passport']: data[fieldIP['passport']],
                    fieldIP['inn']: data[fieldIP['inn']],
                    'id': data['id']}
