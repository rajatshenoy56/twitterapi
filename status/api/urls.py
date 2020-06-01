from django.conf.urls import url
from django.contrib import admin

from .views import (
	StatusListAPIView,
	StatusRetrieveAPIView,
	StatusUpdateAPIView,
	StatusDestroyAPIView,
	StatusCreateAPIView,
	StatusListAllAPIView,
	StatusShareAPIView,
	StatusLikeAPIView,
	)

urlpatterns = [
	url(r'^$', StatusListAPIView.as_view(), name='list'),
	url(r'^create/$',StatusCreateAPIView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$',StatusRetrieveAPIView.as_view(),name='retrieve'),
	url(r'^(?P<pk>\d+)/update/$',StatusUpdateAPIView.as_view(),name='update'),
	url(r'^(?P<pk>\d+)/destroy/$',StatusDestroyAPIView.as_view(),name='destroy'),
	url(r'^list_all/$',StatusListAllAPIView.as_view(),name='list_all'),
	url(r'^share/(?P<pk>\d+)/$',StatusShareAPIView.as_view(), name='share'),
	url(r'^like/(?P<pk>\d+)/$',StatusLikeAPIView.as_view(), name='like'),
]

app_name = 'status-api'