class IPPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        result = {}
        
        physip = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('egrip', {}).get('items', [{}])[0]
        
        result['inn'] = physip.get('inn', '')
        result['state'] = physip.get('state', '-')
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
        result['activity_additional_name'] = physip.get('activity', {}).get('additional', [{}])[0].get('name', '') if physip.get('activity', {}).get('additional', [{}]) != [] else ''

        passport = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('passport', {})
        result['details'] = passport.get('details', '')
        
        cases = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('arbitr_full', {}).get('cases', [{}])[0]
        result['claim_sum'] = cases.get('claim_sum', 0)
        
        
        result['score_state'] = '100' if result['state'] == 'NOT_ACTIVE' else '0'
        result['score_stopash_date'] = '100' if result['stopash_date'] and result['stopash_date'] != '' else '0'
        result['score_claim_sum'] = '100' if int(result['claim_sum']) >= 10000000 else '0'
        
        result['uid'] = data.get('data', [{}])[0].get('uid', '') if data.get('data', [{}]) != [] else ''
         
        return result
    