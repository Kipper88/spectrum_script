from src.Jur.get_data import JurGet
from src.Jur.prepare_data import JurPrepare
from src.Jur.post_data import JurPost
from src.Jur.webhook import RukJurWebhook

from src.Driver.get_data import DriverGet
from src.Driver.prepare_data import DriverPrepare
from src.Driver.post_data import DriverPost
from src.Driver.webhook import RukDriverWebhook

from src.Auto.get_data import AutoGet
from src.Auto.prepare_data import AutoPrepare
from src.Auto.post_data import AutoPost
from src.Auto.webhook import RukAutoWebhook

from src.IP.get_data import IPGet
from src.IP.prepare_data import IPPrepare
from src.IP.post_data import IPPost
from src.IP.webhook import RukIPWebhook

from src.Phys.get_data import PhysGet
from src.Phys.prepare_data import PhysPrepare
from src.Phys.post_data import PhysPost
from src.Phys.webhook import RukPhysWebhook

from src.Globus.get_data import GlobusGet
from src.Globus.prepare_data import GlobusPrepare
from src.Globus.post_data import GlobusPost
from src.Globus.webhook import RukGlobusWebhook

from src.Planning.post_data import PlanningPost
from src.Planning.webhook import RukPlanningWebhook

from settings.cfgRukWebhook import fieldJur as FJurW

from settings.cfgRukWebhook import fieldDriver as DrW

from settings.cfgRukWebhook import fieldAuto as FAW

from settings.cfgRukWebhook import fieldIP as FIPW

from settings.cfgRukWebhook import fieldPhys as PhW

from settings.cfgRukWebhook import fieldGlobus as FGlW

# from settings.cfgRukWebhook import fieldPlanning as FPl

import logging
import asyncio
from logging.handlers import RotatingFileHandler

from const import api_key_api_planning

with open('log/script.log', 'a') as f:
    f.write('Script has been reloaded\n')

logging.basicConfig(
    level=logging.DEBUG,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат вывода логов
    datefmt='%Y-%m-%d %H:%M:%S',  # Формат даты и времени
    handlers=[
        RotatingFileHandler(
            filename='log/script.log', 
            mode='a',              # Режим добавления (append)
            maxBytes=10*1024*1024, # Ограничение в 10 МБ (10 * 1024 * 1024 байт)
            backupCount=5          # Количество резервных файлов (опционально)
        )
    ]
)

async def Jur():
    JurG = JurGet()
    JurPrep = JurPrepare
    JurPos = JurPost()
    try:
        id = await RukJurWebhook().webhookJur()
        if id:
            uid = await JurG.post_spectrum_jur_face(id[FJurW['inn']])
            
            delay = await JurG.get_spectrum_jur_face(uid)
            delay = delay.get('data', [{}])[0].get('progress_wait', 10)
            
            await asyncio.sleep(delay)
            data = await JurG.get_spectrum_jur_face(uid)
                
            data = await JurPrep.prepare_data(data)

            await JurPos.post_data(data, id['id'])
            logging.info('OK Jur')
    except Exception as err:
        logging.error(str(err), exc_info=True)
        
async def Driver():
    DrG = DriverGet()
    DrPrep = DriverPrepare()
    DrPos = DriverPost()
    try:
        # Lic (N1)
        id = await RukDriverWebhook().webhook()
        if id:
            uid = await DrG.post_spectrum(
                id[DrW['DriverLicense']], 
                id[DrW['DriverLicenseDate']], 
                id[DrW['LastName']], 
                id[DrW['FirstName']], 
                id[DrW['Patronymic']],
                id[DrW['Birth']]
            )
                        
            delay = await DrG.get_spectrum(uid)
            delay = delay.get('data', [{}])[0].get('progress_wait', 10)
            
            await asyncio.sleep(delay)
            data = await DrG.get_spectrum(uid)
                
            data = await DrPrep.prepare_data(data)
            
            await DrPos.post_data(data, id['id'])
            logging.info('OK Driver')
            
        # Percent (N2)
        """id = await RukDriverWebhook().webhookPercent()
        if id:
            uid = await DrG.post_spectrum_percent(id[DrW['LastName']], id[DrW['FirstName']], id[DrW['Patronymic']], id[DrW['Birth']])
            data = await DrG.get_spectrum_percent(uid)
            data = await DrPrep.prepare_data_percent(data)
            await DrPos.post_data_percent(data, id['id'])
            logging.info('OK') """
            
    except Exception as err:
        logging.error(str(err), exc_info=True)
        
async def Auto():
    AutoG = AutoGet()
    AutoPrep = AutoPrepare()
    AutoPos = AutoPost()
    try:
        id = await RukAutoWebhook().webhookAuto()
        if id:
            uid = await AutoG.post_spectrum(id[FAW['GRZ']])
            
            delay = await AutoG.get_spectrum(uid)
            delay = delay.get('data', [{}])[0].get('progress_wait', 10)
            
            await asyncio.sleep(delay)
            
            data = await AutoG.get_spectrum(uid)
            data = await AutoPrep.prepare_data(data)
            await AutoPos.post_data(data, id['id'])
            logging.info('OK Auto')
    except Exception as err:
        logging.error(str(err), exc_info=True)

async def IP():
    IPG = IPGet()
    IPPrep = IPPrepare()
    IPPos = IPPost()
    try:
        id = await RukIPWebhook().webhook()
        if id:
            uid = await IPG.post_spectrum(
                id[FIPW['last_name']],
                id[FIPW['first_name']],
                id[FIPW['patronymic']],
                id[FIPW['birth']],
                id[FIPW['passport']],
                id[FIPW['inn']]
                )
            delay = await IPG.get_spectrum(uid)
            delay = delay.get('data', [{}])[0].get('progress_wait', 10)
            
            await asyncio.sleep(delay)
            
            data = await IPG.get_spectrum(uid)
        
            data = await IPPrep.prepare_data(data)
            
            await IPPos.post_data(data, id['id'])
            logging.info('OK IP')
    except Exception as err:
        logging.error(str(err), exc_info=True)
        
async def Phys():
    PhysG = PhysGet()
    PhysPrep = PhysPrepare()
    PhysPos = PhysPost()
    try:
        id = await RukPhysWebhook().webhook()
        if id:
            uid = await PhysG.post_spectrum(
                id[PhW['last_name']],
                id[PhW['first_name']],
                id[PhW['patronymic']],
                id[PhW['birth']],
                id[PhW['passport']],
                id[PhW['passport_date']],
                id[PhW['inn']]
                )
            delay = await PhysG.get_spectrum(uid)
            delay = delay.get('data', [{}])[0].get('progress_wait', 10)
            
            await asyncio.sleep(delay)
            
            data = await PhysG.get_spectrum(uid)
            
            data = await PhysPrep.prepare_data(data)
            
            await PhysPos.post_data(data, id['id'])
            logging.info('OK Phys')
    except Exception as err:
        logging.error(str(err), exc_info=True)
    
async def Globus():
    GlobusG = GlobusGet()
    GlobusPrep = GlobusPrepare()
    GlobusPos = GlobusPost()
    try:
        id = await RukGlobusWebhook().webhook()
        if id:
            data = await GlobusG.get_data(
                id[FGlW['declarant_tin']],
                id[FGlW['start']],
                id[FGlW['finish']],
                id[FGlW['direction']]
                )

            data = await GlobusPrep.prepare_data(data)
            
            await GlobusPos.post_data(data, id['id'])
            logging.info('OK Globus')
    except Exception as err:
        logging.error(str(err), exc_info=True)
        
async def Planning():
    PlanningPos = PlanningPost()  

    try:
        #постоянно опрашиваем руководитель на предмет новых записей
        id = await RukPlanningWebhook().webhook()
        # если найдена новая запись
        if id:
            id.pop('id')
            id['api_key'] = api_key_api_planning
            # постим данные на удаленный сервер
            result = await PlanningPos.post_data(id)
            # место для доп. логики, исходя из ответа сервера апи планирования
            # if result.get('status', '') == 'success':
            #     ...
                
            logging.info('OK Globus')
    except Exception as err:
        logging.error(str(err), exc_info=True)    
        
functions = [
    Jur,
    Driver,
    Auto,
    IP,
    Globus,
    Planning
]
async def main():
    while True:
        await asyncio.gather(*(func() for func in functions))
        await asyncio.sleep(2)
    
if __name__ == "__main__":
    asyncio.run(main())