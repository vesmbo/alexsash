# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class OneSiteDemo(models.Model):
    class Meta():
        db_table = 'app_onesite_demo'
    """
    первое приложение на джанго
    """

    onesitedemo_title = models.CharField(max_length=200, verbose_name='Заголовок')
    onesitedemo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    onesitedemo_date = models.DateTimeField(verbose_name='Дата')

    def __unicode__(self):
        return self.onesitedemo_title


