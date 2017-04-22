from django.conf.urls import url
from django.contrib import admin

from dashboard.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name = 'home'),
	]
