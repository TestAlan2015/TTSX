from django.conf.urls import url
from . import views
from . import views
urlpatterns = [
    url(r'^cart/$',views.cart),
    url(r'^add/$',views.add),
    url(r'^count/$',views.count),
    url(r'^delete/$',views.delete),
    url(r'^update/$',views.update),
]