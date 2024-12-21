from aiohttp import ClientSession
from settings.cfgRukPost import fieldJur
from settings.cfgRukWebhook import fieldJur as FJW
from const import urlRuk, apiKeyRuk

class JurPost:
    def __init__(self):
        ...
        
    async def post_data(self, data, id_f):
        # items = {
        #     fieldJur['activityDuration']: data.get('activity_duration', ''),  # Продолжительность периода деятельности организации
        #     fieldJur['isNotActiveDate']: data.get('is_not_active_date', ''),  # Дата прекращения деятельности
        #     fieldJur['code']: data.get('code', ''),       
        #     fieldJur['name']: data.get('name', ''),
        #     fieldJur['year']: data.get('year', ''),
        #     fieldJur['group']: data.get('group', ''),
        #     fieldJur['total']: data.get('total', ''),
        #     fieldJur['date']: data.get('date', ''),
        #     fieldJur['inclusionDate']: data.get('inclusionDate', ''),
        #     fieldJur['exclusionDate']: data.get('exclusionDate', ''),
        #     fieldJur['reason']: data.get('reason', ''),
        #     fieldJur['actualCaseStatus']: data.get('actualCaseStatus', ''),
        #     fieldJur['net_profit']: data.get('net_profit', ''),
        #     fieldJur['score_is_not_active_date']: data.get('score_is_not_active_date', ''),
        #     fieldJur['score_total']: data.get('score_total', ''),
        #     fieldJur['score_date']: data.get('score_date', ''),
        #     fieldJur['score_inclusionDate']: data.get('score_inclusionDate', ''),
        #     fieldJur['score_actualCaseStatus']: data.get('score_actualCaseStatus', ''),
        #     fieldJur['score_net_profit']: data.get('score_net_profit', ''),
        #     fieldJur['uid']: data.get('uid', '')
        # }
        
        items = {fieldJur[key]: data[key] for key in fieldJur}
            
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
            data = await sess.post(url=urlRuk, 
                                   json=params,
                                   ssl=False)
            
        
