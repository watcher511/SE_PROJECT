from .getPublicData import *
import time
# 获取当前时间
def getNowTime():
    timeFormat = time.localtime()
    yer = timeFormat.tm_year
    mon = timeFormat.tm_mon
    day = timeFormat.tm_mday
    return yer,monthList[mon-1],day
