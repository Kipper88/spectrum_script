from datetime import datetime

class DriverPrepare:
    async def prepare_data(self, data):
        """ВУ. Основное (действительность, срок действия)		Ссылка на документацию: https://my.spectrumdata.ru/docs/520b756e/report-blocks/P.0026.DRL.BAS-TRU\n
        Скоринг правовой благонадёжности. Метод 1		Ссылка на документацию: https://my.spectrumdata.ru/docs/520b756e/report-blocks/P.0103.PBS.ACT-SCR"""
        result = {}
        
        lic = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('cp_driver_license_v2', {}).get('driverLicense', {})
        
        # ВУ. Основное (действительность, срок действия)
        result['endDate'] = lic.get('endDate', '-')    # Срок действия
        result['issuer'] = lic.get('issuer', '-')            # Кем выдано ВУ
        
        result['categories'] = ', '.join(lic.get('categories', []))           # Категория ВУ
        
        percent = data.get('data', [{}])[0].get('content', {}).get('check_person', {}).get('driver_rating', {}).get('scoring', {})
        
        result['pb_percent'] = percent.get('invert_index', '30')
        result['pb_color'] = ""
        
        result["score_endDate"] = '100' if (datetime.strptime(result['endDate'], '%Y-%m-%d').year if result['endDate'] != '-' else 99999) < 2023  else '0'
        
        return result
        
    """ async def prepare_data_percent(self, data):
        Скоринг правовой благонадёжности. Метод 1		Ссылка на документацию: https://my.spectrumdata.ru/docs/520b756e/report-blocks/P.0103.PBS.ACT-SCR
        
        result = {}
        
        data = data.get('data', [{}])[0]['content']['check_person']['proceeding_v2']['executive_v2']['scoring']
        
        result['pb_percent'] = data.get('pb_percent', '')
        result['pb_color'] = data.get('pb_color', '')
        
        return result """