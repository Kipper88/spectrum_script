from aiohttp import ClientSession

from settings.cfgRukPost import fieldGlobus
from settings.cfgRukWebhook import fieldGlobus as FGlW
from const import apiKeyRuk, urlRuk


class GlobusPost:
    def __init__(self):
        ...
        
    async def post_data(self, data, id_f):
        """activity_duration, is_not_active_date,\n
           code, name,\n
           year, group, total,\n
           itemsDate,\n
           inclusionDate, exclusionDate, reason,\n
           actualCaseStatus"""
        
        items = {
            fieldGlobus['country_departure']: data.get('country_departure', '-'),
            fieldGlobus['country_destination']: data.get('country_destination', '-'),
            fieldGlobus['incoterms']: data.get('incoterms', '-'),
            fieldGlobus['price_usd']: data.get('price_usd', '-'),
            fieldGlobus['sender_name']: data.get('sender_name', '-'),
            fieldGlobus['recipient_tin']: data.get('recipient_tin', '-'),
            fieldGlobus['recipient_name']: data.get('recipient_name', '-'),
            fieldGlobus['found']: data.get('found', '-'),
            fieldGlobus['error']: data.get('error', '-')
        }
            
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FGlW['Globus'],                                            # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}                                       # массив записей
        }
        
        async with ClientSession() as sess:
            data = await sess.post(url=urlRuk, json=params)