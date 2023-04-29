from django.contrib.postgres.fields import ArrayField
from django.db import models


class Event(models.Model):
    """ событие """
    name = models.CharField(verbose_name="Название мероприятия", max_length=500)
    description = models.TextField(verbose_name="Описание мероприятия")
    datebegin = models.DateTimeField()
    dateend = models.DateTimeField()
    place = models.CharField(verbose_name="Метсо проведения", max_length=500)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='фотография', null=True, blank=True)
    organizationId = models.IntegerField(verbose_name="ID орагнизации", null=True, blank=True)


class Team(models.Model):
    id_system_team = models.IntegerField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)


class RegionalPartner(models.Model):
    id_system_partner = models.IntegerField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
