from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from dashboard.views import IndexView

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name = 'home'),
	]
