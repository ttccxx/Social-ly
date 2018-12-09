from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(verbose_name='UserID', primary_key=True)
    image = models.ImageField(verbose_name='image', null=True)

    class Meta:
        verbose_name = 'User'

class Calendar(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='date')
    time = models.TimeField(verbose_name='time', default='')
    info = models.CharField(verbose_name='info', max_length=40, default='')

    class Meta:
        verbose_name = 'Calendar'