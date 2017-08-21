"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myproject import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^alko/$', views.alko),
    url(r'^contacts/$', views.contacts),
    url(r'^links/$', views.links),
    url(r'^find/user/add/(?P<ticket_id>\d+)/$', views.user_add),
    url(r'^find/$', views.find),
    url(r'^lcb/user/delete/(?P<ticket_id>\d+)/$', views.user_delete),
    url(r'^lcb/$', views.lcb),
    url(r'^lcb_admin/$', views.lcb_admin),
    url(r'^auth/', include('loginsys.urls')),

]
