from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^info/$',views.info),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
]