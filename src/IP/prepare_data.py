class IPPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        result = {}
        
        physip = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('egrip', {}).get('items', [{}])[0]
        
        with open('json.json', 'w') as f:
            import json
            json.dump(data, f, indent=4)
        
        result['inn'] = physip.get('inn', '')
        result['state'] = physip.get('state', '')
        result['ogrn'] = physip.get('ogrn', '')
        result['ogrn_date'] = physip.get('ogrn_date', '')
        result['date'] = physip.get('date', '')
        result['address_text'] = physip.get('address_text', '')
        result['type'] = physip.get('type', '')
        result['found_by_inn'] = physip.get('found_by_inn', '')
        result['activity_main_name'] = physip.get('activity', {}).get('main', {}).get('name', '')
        result['stopash_date'] = physip.get('stopash_date', '')
        result['lits_type_deyat_name'] = physip.get('lits_type_deyat_name', '')
        
        #result['ogrn_date'] = physip.get('ogrn_date', '')
        result['last_date'] = physip.get('last_date', '')
        result['name_long'] = physip.get('name', {}).get('name', '')
        result['stop_org_date'] = physip.get('stop_org_date', '')
        #result['activity_main_name'] = physip.get('activity', {}).get('main', {}).get('name', '')
        result['activity_additional_name'] = physip.get('activity', {}).get('additional', [{}])[0].get('name', '')

        passport = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('passport', {})
        result['details'] = passport.get('details', '')
        
        return result
    