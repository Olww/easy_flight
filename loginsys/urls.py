import loginsys
from django.conf.urls import url, include
from loginsys import views
from django.contrib import admin

from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    url(r'users/logout/$', auth_views.logout,
        kwargs={'next_page': '/'}, name='auth_logout'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

      url(r'registration/$', views.register, name='register'),

]