import DataController.views as DC


def create(dic, type= 1):
    if type == 1:
        dic = dic.copy()
        event_key = DC.get_event_key(dic['sessionKey'])
        dic['eventKey'] = event_key
        dic['type'] = 1
        return DC.create_calendar(dic)
    else:
        return DC.create_calendar(dic)


def edit(dic):
    DC.edit_calendar(dic)


def delete(dic):
    DC.delete_calendar(dic)


def get(dic):
    return DC.get_calendar(dic)
