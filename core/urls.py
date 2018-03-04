from django.conf.urls import url,include
from django.contrib.auth import views as auth_views

from .views import *
urlpatterns = [
	url(r'^$', home, name='home')
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]