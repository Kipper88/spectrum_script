from aiohttp import ClientSession

from settings.cfgRukPost import fieldAuto
from settings.cfgRukWebhook import fieldAuto as FA
from const import apiKeyRuk, urlRuk

class AutoPost:
    def __init__(self):
        ...
    
    async def post_data(self, data, id_f):
        items = {
            fieldAuto['VIN']: data['VIN'],
            fieldAuto['CTC']: data['CTC'],
            
            fieldAuto['original']: data['original'],
            fieldAuto['colorName']: data['colorName'],
            fieldAuto['year']: data['year'],
            
            fieldAuto['dateReceive']: data['dateReceive'],
            
            fieldAuto['periodEnd']: data['periodEnd'],
            fieldAuto['policyStatus']: data['policyStatus'],
            
            fieldAuto['inclusionDateis_wanted']: data['inclusionDateis_wanted']
        }
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FA['Auto'],                                            # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}
        }
        
        async with ClientSession() as sess:
            await sess.post(url=urlRuk,
                            json=params)