class JurPrepare:
    async def prepare_data(data):
        
        dat = dat.get('data', [{}])[0].get('content', {})
        
        result = {}

        # Сведения о юридическом лице
        result['activityDuration'] =  dat.get('xfirm', {}).get('fns_egrul_egrip', {}).get('org', {}).get('activity_duration', {}).get('text', '')                       # Продолжительность периода деятельности организации
        result['isNotActiveDate'] = dat.get('xfirm', {}).get('fns_egrul_egrip', {}).get('org', {}).get('is_not_active_date', '1111-11-11')                                       # Дата прекращения деятельности
        
        # Сведения о состоянии/статусе
        result['code'] =               dat.get('fns_opendata', {}).get('paytax', {}).get('data', {}).get('paytax', [{}])[0].get('taxes', [{}])[0].get('code', '')        # Код статуса
        result['name'] =               dat.get('fns_opendata', {}).get('paytax', {}).get('data', {}).get('paytax', [{}])[0].get('taxes', [{}])[0].get('name', '')        # Наименование статуса ЮЛ
        
        # Налоговые задолженности организации
        result['year'] =               dat.get('fns_opendata', {}).get('debtam', {}).get('data', {}).get('debtam', [{}])[0].get('year',  '')                             # Год актуальности данных
        result['group'] =              dat.get('fns_opendata', {}).get('debtam', {}).get('data', {}).get('debtam', [{}])[0].get('debts', [{}])[0].get('group', '')       # Название группы, в которую входит налог
        result['total'] =              dat.get('fns_opendata', {}).get('debtam', {}).get('data', {}).get('debtam', [{}])[0].get('debts', [{}])[0].get('total', 0)        # Общая сумма недоимки по налогу, пени и штрафу
        
        # Приостановление операций по счетам контрагента
        result['date'] =               dat.get('xfirm', {}).get('acc_stop', {}).get('items', [{}])[0].get('date', '')                                                    # Дата решения о приостановлении в формате YYYY-DD-MM
        
        # Причастность к включению в реестр недобросовестных поставщиков
        result['inclusionDate'] =      dat.get('xfirm', {}).get('rnp_affected_supplier', {}).get('affectedSuppliers', [{}])[0].get('inclusionDate', '')                  # Дата включения сведений в реестр
        result['exclusionDate'] =      dat.get('xfirm', {}).get('rnp_affected_supplier', {}).get('affectedSuppliers', [{}])[0].get('exclusionDate', '')                  # Дата исключения сведений из реестра
        result['reason'] =             dat.get('xfirm', {}).get('rnp_affected_supplier', {}).get('affectedSuppliers', [{}])[0].get('reason', '')                         # Причина для включения в реестр

        # Банкротство юрлица: краткий отчёт
        result['actualCaseStatus'] =   dat.get('xfirm', {}).get('bankruptcy_short', {}).get('actualCaseStatus', {}).get('description', '')
        
        # Финансовая отчетность организации
        items = dat.get('xfirm', {}).get('fns_bfo_full', {}).get('fullReports', [{}])[0].get('items', [{}])
        result['net_profit'] = next((str(item.get("value", '0')) for item in items if item.get("description") == "Чистая прибыль (убыток)"), '0')
     
        # Баллы 
        result['score_is_not_active_date'] = '100' if result['isNotActiveDate'] != '' and result['isNotActiveDate'] != '1111-11-11' else '0'
        result['score_total'] =              '100' if int(result['total']) >= 500000 else '0'
        result['score_date'] =               '100' if result['date'] != '' else '0'
        result['score_inclusionDate'] =      '100' if result['inclusionDate'] != '' else '0'
        result['score_actualCaseStatus'] =   '100' if result['actualCaseStatus'] != '' else '0'
        result['score_net_profit'] =         '100' if int(result['net_profit']) < 0 else '0'
        
        result['uid'] = data.get('data', [{}])[0].get('uid', '')
            
        return result