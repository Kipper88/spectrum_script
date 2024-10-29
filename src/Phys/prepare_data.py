class PhysPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        result = {}
        
        arbitr = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('arbitr_short', {})
        result['cases_amount_total'] = arbitr.get('cases_amount_total', '-')
        result['plaintiff_cases_amount'] = arbitr.get('plaintiff_cases_amount', '-')
        result['plaintiff_cases_sum'] = arbitr.get('plaintiff_cases_sum', '-')
        result['defendant_cases_amount'] = arbitr.get('defendant_cases_amount', '-')
        result['defendant_cases_sum'] = arbitr.get('defendant_cases_sum', '-')
        
        
        registry = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('passport', {})
        result['details_pass'] = registry.get('details', '-')
        
        
        inn = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('inn', {})
        result['value_inn'] = inn.get('value', '-')
        
        
        tax = {} if data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('tax_accrual', {}).get('tax_accruals', [{}]) == [] else\
            data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('tax_accrual', {}).get('tax_accruals', [{}])[0]
        result['amount'] = tax.get('amount', '-')
        result['payment_status'] = tax.get('payment_status', '-')
        result['details'] = tax.get('details', '-')
        result['amount_to_pay'] = tax.get('amount_to_pay', '-')
        
        
        acc_stop = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('acc_stop')
        result['type_name'] = acc_stop.get('items', [{}])[0].get('type', {}).get('name', '-')
        
        
        status = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('statusnpd_nalog', {})
        result['message'] = status.get('message', '-')
        
        
        egrip = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('egrip', {}).get('items', [{}])[0]
        result['ogrn_date'] = egrip.get('ogrn_date', '-')
        result['activity_duration'] = egrip.get('activity_duration', {}).get('text', '-')
        result['stopash_date'] = egrip.get('stopash_date', '-')
        
        
        egrul = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('egrul', {})
        result['last_date'] = egrul.get('last_date', '')
        result['management_position_name'] = egrul.get('management', {}).get('position', {}).get('name', '-')
        result['stop_org_date'] = egrul.get('stop_org_date', '-')
        
        inoagent = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('inoagent', {})
        result['items_isActive'] = inoagent.get('items', [{}])[0].get('isActive', '-')
        
        linkasso_person = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('linkasso_person_relation', {})
        result['throughBy_inn'] = linkasso_person.get('throughBy', {}).get('inn', '-')
        result['position'] = linkasso_person.get('position', '-')
        result['toDate'] = linkasso_person.get('toDate', '-')
        
        return result
    