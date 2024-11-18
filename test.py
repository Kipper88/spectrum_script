from settings.cfgRukPost import fieldAuto

data = {'VIN': 'XU42824DHM0000933', 'CTC': '9935231072', 'original': '2824Dh', 'colorName': 'Белый', 'year': 2021, 'dateReceive': '2021-06-15 00:00:00', 'periodEnd': '2025-07-25', 'policyStatus': 'Действует', 'inclusionDateis_wanted': False, 'score_year': '0', 'score_periodEnd': '0', 'score_inclusionDateis_wanted': '0'}
# Создание нового словаря на основе fieldAuto и data
items = {fieldAuto[key]: data[key] for key in fieldAuto}

print(items)