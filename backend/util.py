from datetime import datetime
def getDate():
    now = datetime.now()
    Date = now.strftime("%y%m%d")
    return Date