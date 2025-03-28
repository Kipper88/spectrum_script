import json
from aiohttp import ClientSession

from const import apiKeyRuk, urlRuk, usernameRuk, passRuk
from settings.cfgRukWebhook import fieldPlanning

async def readJsonFilePlanning():
    with open('temp/idsPlanning.json', 'r', encoding='utf-8') as f:
        js = json.load(f)
    if len(js.keys()) > 100:
        del js['ids'][0]
        json.dump(js, f, indent=4)
    return js

async def checkJsonPlanning(js, id) -> bool:
    if id not in js['ids']:
        js['ids'].append(id)
        with open('temp/idsPlanning.json', 'w', encoding='utf-8') as f:
            json.dump(js, f, indent=4)
        return True
    return None

class RukPlanningWebhook:
    def __init__(self):
        self.urlRuk = urlRuk
        self.apiKey = apiKeyRuk
        self.usernameRuk = usernameRuk
        self.passRuk = passRuk
        
    async def webhook(self):
        params = {
            'key': self.apiKey,
            'username': self.usernameRuk,
            'password': self.passRuk,
            'action': 'select',
            'entity_id': fieldPlanning['Planning'], 
            'select_fields': f"\
                            {fieldPlanning['room']},\
                            {fieldPlanning['start_date_time']},\
                            {fieldPlanning['end_date_time']},\
                            {fieldPlanning['event_name']}"
                            
        }
    
        async with ClientSession() as sess:
            resp = await sess.get(url=self.urlRuk,
                                  json=params,
                                  ssl=False
                                  )
            data = await resp.json(content_type='text/html')
            data = data['data'][-1]
        
        js = await readJsonFilePlanning()
        
        def parse_date_time(datetime_str):
            parts = datetime_str.split(' ', 1)  # Разделяем по первому пробелу
            return {
                'date': parts[0] if len(parts) > 0 else '',
                'time': parts[1] if len(parts) > 1 else ''
            }

        # Пример использования
        
        if await checkJsonPlanning(js, data['id']):
            start_date_time = parse_date_time(data[fieldPlanning['start_date_time']])
            end_date_time = parse_date_time(data[fieldPlanning['end_date_time']])
            return {'room': data[fieldPlanning['room']], 
                    'date': start_date_time['date'],
                    'time': f"{start_date_time['time']}-{end_date_time['time']}",
                    'event_name': data[fieldPlanning['event_name']],
                    'company': "БТГ+",
                    'status': 'Занято',
                    'id': data['id']}
