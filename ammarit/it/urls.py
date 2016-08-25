from django.conf.urls import include, url
from it import views, actions

urlpatterns = [
    # views
    url(r'^$', views.index, name='index'),
    url(r'^adminview', views.adminindex, name='adminview'),
    url(r'^reqview', views.reqview, name='reqview'),
    url(r'^employeeview', views.employeeview, name='employeeview'),
    url(r'^inventoryview', views.inventoryview, name='inventoryview'),
    url(r'^additemview', views.additemview, name='additemview'),
    url(r'^adminlog', views.log, name='log'),
    url(r'^user/(?P<userid>\w+)', views.user, name='user'),

    # actions
    url(r'^login', actions.login_action, name='login'),
    url(r'^logout', actions.logout_action, name='logout'),
    url(r'^makerequest', actions.makerequest, name='makerequest'),
    url(r'^accept_req', actions.accept_req, name='accept_req'),
    url(r'^reject_req', actions.reject_req, name='reject_req'),
    url(r'^return_item', actions.return_item, name='return_item'),
    url(r'^lost_item', actions.lost_item, name='lost_item'),
    url(r'^delete_user', actions.delete_user, name='delete_user'),
    url(r'^addnewitem', actions.addnewitem, name='addnewitem'),
    url(r'^restockitem', actions.restockitem, name='restockitem'),
]
