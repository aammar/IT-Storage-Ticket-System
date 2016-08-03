from django.conf.urls import include, url
from it import views, actions

urlpatterns = [
    # views
    url(r'^$', views.index, name='index'),
    url(r'^adminview', views.adminindex, name='adminview'),
    url(r'^reqview', views.reqview, name='reqview'),
    url(r'^employeeview', views.employeeview, name='employeeview'),
    url(r'^user/(?P<userid>\w+)', views.user, name='user'),

    # actions
    url(r'^makerequest', actions.makerequest, name='makerequest'),
    url(r'^accept_req', actions.accept_req, name='accept_req'),
    url(r'^reject_req', actions.reject_req, name='reject_req'),
]
