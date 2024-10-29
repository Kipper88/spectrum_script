class AutoPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        data = data.get('data', [{}])[0].get('content', {})
        
        data['VIN'] = data.get('identifiers', {}).get('vehicle', {}).get('vin', '')
        data['CTC'] = data.get('identifiers', {}).get('vehicle', {}).get('sts', '')
        
        data['original'] = data.get('tech_data', {}).get('brand', {}).get('name', {}).get('original', '')
        data['colorName'] = data.get('tech_data', {}).get('body', {}).get('color', {}).get('name', '')
        data['year'] = data.get('tech_data', {}).get('year', '')

        data['dateReceive'] = data.get('additional_info', {}).get('vehicle', {}).get('sts', {}).get('date', {}).get('receive', '')

        data['periodEnd'] = data.get('insurance', {}).get('osago', {}).get('items', [{}])[0].get('date', {}).get('periods', [{}])[0].get('end', '')
        data['policyStatus'] = data.get('insurance', {}).get('osago', {}).get('items', [{}])[0].get('policy', {}).get('status', '')

        data['inclusionDateis_wanted'] = data.get('inclusionDateis_wanted', '')
        
        return data