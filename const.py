from dotenv import dotenv_values

vars = dotenv_values('.env')

URL_FOR_POST_DATA_TO_SPECTRUM = 'https://b2b-api.spectrumdata.ru/b2b/api/v1/user/reports/{}/_make'
URL_FOR_REFRESH_DATA_FROM_SPECTRUM = 'https://b2b-api.spectrumdata.ru/b2b/api/v1/user/reports/{}/_refresh'
URL_FOR_GET_DATA_FROM_SPECTRUM = 'https://b2b-api.spectrumdata.ru/b2b/api/v1/user/reports'

api_key_spec = vars.get('api_key_spec', '')

apiKeyRuk = vars.get('apiKeyRuk', '')
urlRuk = 'https://btg-sped.ru/crm/api/rest.php'
usernameRuk = vars.get('usernameRuk', '')
passRuk = vars.get('passRuk', '')

apiKeyGlobus = vars.get('apiKeyGlobus', '')
urlGlobus = 'https://glbs.io/api/supplies-search'


type_request_kontrAgent = vars.get('type_request_kontrAgent', '')
type_request_auto = vars.get('type_request_auto', '')
type_request_dl = vars.get('type_request_dl', '')
type_request_passport = vars.get('type_request_passport', '')
type_request_credit_history = vars.get('type_request_credit_history', '')

NEGATIVE_SCORE_VALUE = '0'
NORMAL_SCORE_VALUE = '100'
NONE_SCORE_VALUE = '30'

urlApiPlanning = 'http://127.0.0.1:5000/api/add_record'
api_key_api_planning = vars.get('api_key_api_planning', '')