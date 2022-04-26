from django.conf.urls import url
from django.conf.urls.static import static 
from . import views


urlpatterns = [
	url(r'^$', views.list, name='list'),
	url('build_kml', views.build_kml, name='build_kml'),
	url('clear_all', views.clear_all, name='clear_all')
] 
