class GlobusPrepare:
    def __init__(self):
        ...
        
    async def prepare_data(self, data):
        result = {}
                
        key = data.get('search', {}).get('result', [{}])
        result['country_departure'] = ", ".join(set([d.get('country_departure', '-') for d in key]))
        result['country_destination'] = ", ".join(set([d.get('country_destination', '-') for d in key]))
        result['incoterms'] = ", ".join(set([d.get('incoterms', '-') for d in key]))
        result['price_usd'] = str(sum(float(d.get('price_usd', 0)) for d in key))
        result['sender_name'] = ", ".join(set([d.get('sender_name', '-') for d in key]))
        result['recipient_tin'] = ", ".join(set([d.get('recipient_tin', '-') for d in key]))
        result['recipient_name'] = ", ".join(set([d.get('recipient_name', '-') for d in key]))
        result['found'] = data.get('search', {}).get('found', 0)
        
        result['error'] = data.get('error', 'Нет ошибок')
        
        return result