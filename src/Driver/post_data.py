from aiohttp import ClientSession

from settings.cfgRukPost import fieldDriver
from settings.cfgRukWebhook import fieldDriver as FDW
from const import urlRuk, apiKeyRuk

class DriverPost:
    def __init__(self):
        ...
    async def post_data(self, data, id_f):
        items = {
            fieldDriver['endDate']: data['endDate'],
            fieldDriver['issuer']: data['issuer'],
            fieldDriver['categories']: data['categories'],
            fieldDriver['pb_percent']: data['pb_percent'],
            fieldDriver['pb_color']: data['pb_color']
        }
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FDW['Drivers'],                                            # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}
        }
        async with ClientSession() as sess:
            await sess.post(url=urlRuk,
                            json=params)
            
    """ async def post_data_percent(self, data, id_f):
        items = {
            fieldDriver['pb_percent']: data['pb_percent'],
            fieldDriver['pb_color']: data['pb_color']
        }
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FDW['Driver'],                                            # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}
        }
        async with ClientSession() as sess:
            await sess.post(url=urlRuk,
                            json=params) """