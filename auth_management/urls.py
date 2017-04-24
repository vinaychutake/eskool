from django.conf.urls import url
from django.contrib.auth import views as auth_views

from auth_management.views import ForgotPassword

urlpatterns = [

    url(r'^login/$', auth_views.login,
    	{'template_name': 'login.html'},
    	name='login'),

    url(r'^logout/$', auth_views.logout,
    	{'template_name': 'logged_out.html'},
    	name='logout'),

    url(r'^forgot-password/$', ForgotPassword.as_view(),
    	name='forgot_password'),

]