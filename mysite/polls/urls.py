#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]
