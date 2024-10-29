from aiohttp import ClientSession
from settings.cfgRukPost import fieldJur
from settings.cfgRukWebhook import fieldJur as FJW
from const import urlRuk, apiKeyRuk

class JurPost:
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
            fieldJur['activityDuration']: data.get('activity_duration', ''),  # Продолжительность периода деятельности организации
            fieldJur['isNotActiveDate']: data.get('is_not_active_date', ''),  # Дата прекращения деятельности
            fieldJur['code']: data.get('code', ''),       
            fieldJur['name']: data.get('name', ''),
            fieldJur['year']: data.get('year', ''),
            fieldJur['group']: data.get('group', ''),
            fieldJur['total']: data.get('total', ''),
            fieldJur['date']: data.get('date', ''),
            fieldJur['inclusionDate']: data.get('inclusionDate', ''),
            fieldJur['exclusionDate']: data.get('exclusionDate', ''),
            fieldJur['reason']: data.get('reason', ''),
            fieldJur['actualCaseStatus']: data.get('actualCaseStatus', '')    
        }
            
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FJW['Jur'],                                            # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}                                       # массив записей
        }
        
        async with ClientSession() as sess:
            data = await sess.post(url=urlRuk, json=params)
            
        