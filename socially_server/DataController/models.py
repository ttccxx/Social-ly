from django.db import models


class User(models.Model):
    session_key = models.IntegerField(default=0)
    event_key = models.IntegerField(default=0)

    def get_session_key(self):
        return self.session_key

    def new_event(self):
        self.event_key += 1
        return self.event_key

    def __str__(self):
        return "sessionKey:%d, eventKey:%d" % (self.session_key, self.event_key)


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_key = models.IntegerField(default=0)
    date = models.DateField()
    time = models.TimeField(default='')
    thing = models.CharField(default='', max_length=60)
    place = models.CharField(default='', max_length=60)
    type = models.IntegerField(default=1)

    def json_dic(self):
        dic = dict()
        dic['thing'] = self.thing
        dic['date'] = self.get_date_str()
        dic['time'] = self.get_time_str()
        dic['eventKey'] = self.get_key_str()
        dic['place'] = self.place
        return dic

    def get_key_str(self):
        return "%03d" % self.event_key

    def get_date_str(self):
        return self.date.strftime("%Y-%m-%d")

    def get_time_str(self):
        return self.time.strftime("%H:%M")

    # def __str__(self):
    #     return "user_key: %d" % self.user.get_session_key() + ", date:" + self.get_date_str() \
    #            + ", time:" + self.get_time_str() + ", eventKey:" + self.get_key_str() \
    #            + ", place:" + self.place


def show_data():
    for user in User.objects.all():
        print(user)
        for event in Calendar.objects.filter(user=user):
            print("\t%s" % event)


class Invitation(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inviter')
    event_key = models.IntegerField(default=0)
    date = models.DateField(verbose_name='date')
    time = models.TimeField(verbose_name='time', default='')
    thing = models.CharField(verbose_name='thing', max_length=60, default='')
    place = models.CharField(default='', max_length=60)
    invitee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='invitee')

    def json_dic(self):
        dic = dict()
        dic['thing'] = self.thing
        dic['date'] = self.get_date_str()
        dic['time'] = self.get_time_str()
        dic['eventKey'] = self.get_key_str()
        dic['place'] = self.place
        # dic['inviter'] = self.inviter
        # dic['invitee'] = self.invitee
        return dic

    def get_key_str(self):
        return "%03d" % self.event_key

    def get_date_str(self):
        return self.date.strftime("%Y-%m-%d")

    def get_time_str(self):
        return self.time.strftime("%H:%M")


    # def __str__(self):
    #     return "inviter_key: %d" % self.inviter.get_session_key() + ", date:" + self.get_date_str() \
    #            + ", time:" + self.get_time_str() + ", eventKey:" + self.get_key_str() \
    #            + ", place:" + self.place + ", invitee_key: %d" % self.invitee.get_session_key()