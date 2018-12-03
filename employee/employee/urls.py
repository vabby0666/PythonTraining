from django.conf.urls import url
from employeeportal import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^employeeupdate/$', views.update, name='update'),
    url(r'^employeeadd/$', views.add, name='add'),
    url(r'^employee/$', views.showTable, name='showTable'),
    url(r'^employee/(?P<item_id>[a-zA-Z0-9]+)/delete/$', views.objectDelete, name='delete_object'),
    url(r'^employee/(?P<item_id>[a-zA-Z0-9]+)/update/$', views.objectUpdate, name='update_object'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^employeesearch/$', views.objectSearch, name='objectSearch'),
]

