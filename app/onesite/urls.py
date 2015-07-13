# -*- coding: utf-8 -*-
__author__ = 'alex'
from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'app.onesite.views.one_site_all', name='all'),
]
