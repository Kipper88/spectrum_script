from datetime import datetime
class AutoPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        data = data.get('data', [{}])[0].get('content', {})
        result = {}
        
        result['VIN'] = data.get('identifiers', {}).get('vehicle', {}).get('vin', '')
        result['CTC'] = data.get('identifiers', {}).get('vehicle', {}).get('sts', '')
        
        result['original'] = data.get('tech_data', {}).get('brand', {}).get('name', {}).get('original', '')
        result['colorName'] = data.get('tech_data', {}).get('body', {}).get('color', {}).get('name', '')
        result['year'] = data.get('tech_data', {}).get('year', datetime.now().year)

        result['dateReceive'] = data.get('additional_info', {}).get('vehicle', {}).get('sts', {}).get('date', {}).get('receive', '-')

        result['periodEnd'] = data.get('insurance', {}).get('osago', {}).get('items', [{}])[0].get('date', {}).get('periods', [{}])[0].get('end', '-')
        result['policyStatus'] = data.get('insurance', {}).get('osago', {}).get('items', [{}])[0].get('policy', {}).get('status', '-')

        result['inclusionDateis_wanted'] = data.get('stealings', {}).get('is_wanted', False)
        
        
        result['score_year'] = '100' if result['year'] != '' and int(result['year']) < datetime.now().year - 19 else '0'
        result['score_periodEnd'] = '100' if result['periodEnd'] and datetime.strptime(result['periodEnd'], "%Y-%m-%d").date() <= datetime.now().date() else '0'
        result['score_inclusionDateis_wanted'] = '100' if result['inclusionDateis_wanted'] != '' and result['inclusionDateis_wanted'] is True else '0'
                
        return result