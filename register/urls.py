from django.conf.urls import include, url
from register import views
from register.views import *

urlpatterns =[
    url(r'^$', UserRegistrationView.as_view(),name='signup'),
    url(r'^success/$', UserRegistrationSucessView.as_view(),name='signup_success'),
    url(r'^dash/$', UserDashboardView.as_view(),name='dash'),


              ]