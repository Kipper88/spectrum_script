class JurPrepare:
    async def prepare_data(dat):
        
        dat = dat.get('data', [{}])[0].get('content', {})
        
        result = {}

        # Сведения о юридическом лице
        result['activity_duration'] =  dat.get('xfirm', {}).get('fns_egrul_egrip', {}).get('org', {}).get('activity_duration', {}).get('text', '')                       # Продолжительность периода деятельности организации
        result['is_not_active_date'] = dat.get('xfirm', {}).get('fns_egrul_egrip', {}).get('org', {}).get('is_not_active_date', '')                                      # Дата прекращения деятельности
        
        # Сведения о состоянии/статусе
        result['code'] =               dat.get('fns_opendata', {}).get('paytax', {}).get('data', {}).get('paytax', [{}])[0].get('taxes', [{}])[0].get('code', '')        # Код статуса
        result['name'] =               dat.get('fns_opendata', {}).get('paytax', {}).get('data', {}).get('paytax', [{}])[0].get('taxes', [{}])[0].get('name', '')        # Наименование статуса ЮЛ
        
        # Налоговые задолженности организации
        result['year'] =               dat.get('fns_opendata', {}).get('debtam', {}).get('data', {}).get('debtam', [{}])[0].get('year',  {})                             # Год актуальности данных
        result['group'] =              dat.get('fns_opendata', {}).get('debtam', {}).get('data', {}).get('debtam', [{}])[0].get('debts', [{}])[0].get('group', '')       # Название группы, в которую входит налог
        result['total'] =              dat.get('fns_opendata', {}).get('debtam', {}).get('data', {}).get('debtam', [{}])[0].get('debts', [{}])[0].get('total', '')       # Общая сумма недоимки по налогу, пени и штрафу
        
        # Приостановление операций по счетам контрагента
        result['date'] =               dat.get('xfirm', {}).get('acc_stop', {}).get('items', [{}])[0].get('date', '')                                                    # Дата решения о приостановлении в формате YYYY-DD-MM
        
        # Причастность к включению в реестр недобросовестных поставщиков
        result['inclusionDate'] =      dat.get('xfirm', {}).get('rnp_affected_supplier', {}).get('affectedSuppliers', [{}])[0].get('inclusionDate', '')                  # Дата включения сведений в реестр
        result['exclusionDate'] =      dat.get('xfirm', {}).get('rnp_affected_supplier', {}).get('affectedSuppliers', [{}])[0].get('exclusionDate', '')                  # Дата исключения сведений из реестра
        result['reason'] =             dat.get('xfirm', {}).get('rnp_affected_supplier', {}).get('affectedSuppliers', [{}])[0].get('reason', '')                         # Причина для включения в реестр

        # Банкротство юрлица: краткий отчёт
        result['actualCaseStatus'] =   dat.get('xfirm', {}).get('bankruptcy_short', {}).get('actualCaseStatus', {}).get('description', '')
            
        return result