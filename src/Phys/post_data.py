from aiohttp import ClientSession

from settings.cfgRukPost import fieldPhys
from settings.cfgRukWebhook import fieldPhys as FPhW
from const import apiKeyRuk, urlRuk


class PhysPost:
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
            fieldPhys['cases_amount_total']: data.get('cases_amount_total', '-'),
            fieldPhys['plaintiff_cases_amount']: data.get('plaintiff_cases_amount', '-'),
            fieldPhys['plaintiff_cases_sum']: data.get('plaintiff_cases_sum', '-'),
            fieldPhys['defendant_cases_amount']: data.get('defendant_cases_amount', '-'),
            fieldPhys['defendant_cases_sum']: data.get('defendant_cases_sum', '-'),
            
            fieldPhys['details_pass']: data.get('details_pass', '-'),
  
            fieldPhys['value_inn']: data.get('value_inn', '-'),
            
            fieldPhys['amount']: data.get('amount', '-'),
            fieldPhys['payment_status']: data.get('payment_status', '-'),
            fieldPhys['details']: data.get('details', '-'),
            fieldPhys['amount_to_pay']: data.get('amount_to_pay', '-'),
            
            fieldPhys['type_name']: data.get('type_name', '-'),
            
            fieldPhys['message']: data.get('message', '-'),
            
            fieldPhys['ogrn_date']: data.get('ogrn_date', '-'),
            fieldPhys['activity_duration']: data.get('activity_duration', '-'),
            fieldPhys['stopash_date']: data.get('stopash_date', '-'),
            
            fieldPhys['last_date']: data.get('stopash_date', '-'),
            fieldPhys['management_position_name']: data.get('management_position_name', '-'),
            fieldPhys['stop_org_date']: data.get('stop_org_date', '-'),
            
            fieldPhys['items_isActive']: data.get('items_isActive', '-'),
            
            fieldPhys['throughBy_inn']: data.get('throughBy_inn', '-'),
            fieldPhys['position']: data.get('position', '-'),
            fieldPhys['toDate']: data.get('toDate', '-')
        }
            
        params = {
            'key': apiKeyRuk,           # API ключ  
            'username': 'PortalBTG24',                                   # Имя пользователя
            'password': 'PortalBTG2024',                                 # Пароль
            'action': 'update',                                          # действие
            'entity_id': FPhW['Phys'],                                   # ID сущности, в которую будет добавлена запись                                       # ID подсущности, в которую будет добавлена запись
            'data': items,
            'update_by_field': {'id': id_f}                              # массив записей
        }
        
        async with ClientSession() as sess:
            data = await sess.post(url=urlRuk, json=params)