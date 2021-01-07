from django.conf.urls import url
from . import views
from django.conf.urls.static import statics

urlpatterns = [
	url(r'^$', views.list, name='list'),
	url('build_kml', views.build_kml, name='build_kml'),
	url('clear_all', views.clear_all, name='clear_all')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
