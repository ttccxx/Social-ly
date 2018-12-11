import DataController.views as DC


def create(dic):
    return DC.create_calendar(dic['sessionKey'], dic['date'], dic['time'], dic['thing'], dic['place'])


def edit(dic):
    DC.edit_calendar(dic['sessionKey'], dic['eventKey'], dic['date'], dic['time'], dic['thing'], dic['place'])


def delete(dic):
    DC.delete_calendar(dic['sessionKey'], dic['eventKey'])


def get(dic):
    return DC.get_calendar(int(dic['sessionKey']))
