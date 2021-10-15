from datetime import datetime
from dateutil import tz
import re


abc = tz.gettz('Europe/London')
dat = datetime.now(abc)
dt_string = dat.strftime("%d-%b-%Y %H:%M:%S")
log.info(dt_string + " +0100")
