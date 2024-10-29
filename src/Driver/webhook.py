from aiohttp import ClientSession
from datetime import datetime
import json

from settings.cfgRukWebhook import fieldDriver
from const import apiKeyRuk, urlRuk

async def readJsonFileLic():
    with open('temp/idsDriverLic.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonLic(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsDriverLic.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return False
        
async def readJsonFilePercent():
    with open('temp/idsDriverPercent.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonPercent(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsDriverPercent.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return None
    
    

class RukDriverWebhook:
    def __init__(self):
        self.urlRuk = urlRuk
        self.apiKey = apiKeyRuk
        
    async def webhook(self):
        
        params = {
            'key': 'qtIeyLiuELr77ptCXcL3RhHhVNJscQvXzvyOcaIC',  # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldDriver['Drivers'], 
            'select_fields': f"{fieldDriver['DriverLicense']}, {fieldDriver['DriverLicenseDate']}, {fieldDriver['LastName']}, {fieldDriver['FirstName']}, {fieldDriver['Patronymic']}, {fieldDriver['Birth']}",
            #'filters': {
            #    '159': datetime.now().strftime('%Y-%m-%d')
            #}
            }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  json=params
                                  )
            
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFileLic()
        
        if await checkJsonLic(js, data['id']):
            return {
                fieldDriver['DriverLicense']: data[fieldDriver['DriverLicense']], 
                fieldDriver['DriverLicenseDate']: data[fieldDriver['DriverLicenseDate']],
                fieldDriver['LastName']: data[fieldDriver['LastName']], 
                fieldDriver['FirstName']: data[fieldDriver['FirstName']],
                fieldDriver['Patronymic']: data[fieldDriver['Patronymic']], 
                fieldDriver['Birth']: data[fieldDriver['Birth']],
                'id': data['id']
            }
            
    """ async def webhookPercent(self):
        params = {
            'key': 'qtIeyLiuELr77ptCXcL3RhHhVNJscQvXzvyOcaIC',  # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                   # Пароль
            'action': 'select',                                    # действие
            'entity_id': fieldDriver['Drivers'], 
            'select_fields': f"{fieldDriver['LastName']}, {fieldDriver['FirstName']}, {fieldDriver['Patronymic']}, {fieldDriver['Birth']}",
            #'filters': {
            #    '159': datetime.now().strftime('%Y-%m-%d')
            #}
            # ID сущности, в которую будет добавлена запись
        }
        
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  json=params
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFilePercent()
        if await checkJsonPercent(js, data['id']):
            return {fieldDriver['LastName']: data[fieldDriver['LastName']], fieldDriver['FirstName']: data[fieldDriver['FirstName']], fieldDriver['Patronymic']: data[fieldDriver['Patronymic']], fieldDriver['Birth']: data[fieldDriver['Birth']], 'id': data['id']} """