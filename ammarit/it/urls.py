from django.conf.urls import include, url
from it import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^makerequest', views.makerequest, name='makerequest'),
    url(r'^adminview', views.adminindex, name='adminview')
]
