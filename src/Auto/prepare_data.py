from datetime import datetime
from const import NEGATIVE_SCORE_VALUE, NORMAL_SCORE_VALUE
class AutoPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        data = data.get('data', [{}])[0].get('content', {})
        result = {}
        
        result['VIN'] = data.get('identifiers', {}).get('vehicle', {}).get('vin', '-')
        result['CTC'] = data.get('identifiers', {}).get('vehicle', {}).get('sts', '-')
        
        result['original'] = data.get('tech_data', {}).get('brand', {}).get('name', {}).get('original', '-')
        result['colorName'] = data.get('tech_data', {}).get('body', {}).get('color', {}).get('name', '-')
        result['year'] = data.get('tech_data', {}).get('year', '-')

        result['dateReceive'] = data.get('additional_info', {}).get('vehicle', {}).get('sts', {}).get('date', {}).get('receive', '-')

        result['periodEnd'] = data.get('insurance', {}).get('osago', {}).get('items', [{}])[0].get('date', {}).get('periods', [{}])[0].get('end', '-')
        result['policyStatus'] = data.get('insurance', {}).get('osago', {}).get('items', [{}])[0].get('policy', {}).get('status', '-')

        result['inclusionDateis_wanted'] = data.get('stealings', {}).get('is_wanted', '-')
        
        
        result['score_year'] = (NORMAL_SCORE_VALUE if int(result['year']) < datetime.now().year - 19 else NEGATIVE_SCORE_VALUE) if (result['year'] != '' and result['year'] != '-') else NEGATIVE_SCORE_VALUE
        result['score_periodEnd'] = (NORMAL_SCORE_VALUE if datetime.strptime(result['periodEnd'], "%Y-%m-%d").date() <= datetime.now().date() else NEGATIVE_SCORE_VALUE) if (result['periodEnd'] != '-' and result['year'] != '') else NEGATIVE_SCORE_VALUE
        result['score_inclusionDateis_wanted'] = (NORMAL_SCORE_VALUE if result['inclusionDateis_wanted'] is True else NEGATIVE_SCORE_VALUE) if result['inclusionDateis_wanted'] != False and result['inclusionDateis_wanted'] != '-' else NEGATIVE_SCORE_VALUE
                
        return result