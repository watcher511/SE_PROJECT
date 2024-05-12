from app01.models import *

monthList=['January','Februry','March','April',
           'May','June','July','August',
           'September','October','November','December']
def getAllUsers():
    return Account.objects.all()

def getAllStaff():
    return Staff.objects.all()