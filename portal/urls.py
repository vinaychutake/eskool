from django.conf.urls import url
from django.contrib import admin

from portal.views import LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name = 'landing_page'),
]


