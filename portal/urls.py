from django.conf.urls import url
from django.contrib import admin
from portal import views as portal_views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', portal_views.LandingView.as_view(), name = 'landing_page'),
]


