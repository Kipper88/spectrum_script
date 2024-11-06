from aiohttp import ClientSession

from settings.cfgRukPost import fieldIP
from settings.cfgRukWebhook import fieldIP as FIPW
from const import apiKeyRuk, urlRuk


class IPPost:
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
            fieldIP['inn']: data.get('inn', ''),  # Продолжительность периода деятельности организации
            fieldIP['state']: data.get('state', ''),  # Дата прекращения деятельности
            fieldIP['ogrn']: data.get('ogrn', ''),       
            fieldIP['ogrn_date']: data.get('ogrn_date', ''),
            fieldIP['date']: data.get('date', ''),
            fieldIP['address_text']: data.get('address_text', ''),
            fieldIP['type']: data.get('type', ''),
            fieldIP['found_by_inn']: data.get('found_by_inn', ''),
            fieldIP['activity_main_name']: data.get('activity_main_name', ''),
            fieldIP['stopash_date']: data.get('stopash_date', ''),
            fieldIP['lits_type_deyat_name']: data.get('lits_type_deyat_name', ''),
            
            fieldIP['details']: data.get('details', ''),
            
            fieldIP['last_date']: data.get('last_date', ''),
            fieldIP['name_long']: data.get('name_long', ''),
            fieldIP['stop_org_date']: data.get('stop_org_date', ''),
            fieldIP['activity_additional_name']: data.get('activity_additional_name', '')
        }
            
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FIPW['IP'],                                            # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}                                       # массив записей
        }
        
        async with ClientSession() as sess:
            data = await sess.post(url=urlRuk, 
                                   json=params,
                                   ssl=False)