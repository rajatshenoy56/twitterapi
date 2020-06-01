from django.conf.urls import url
from django.contrib import admin

from .views import (
	CommentListAPIView,
	CommentCreateAPIView
	)

urlpatterns = [
	url(r'^$', CommentListAPIView.as_view(), name='list'),
	url(r'^create/(?P<pk>\d+)/$',CommentCreateAPIView.as_view(), name='create'),
# 	url(r'^(?P<pk>\d+)/$',StatusRetrieveAPIView.as_view(),name='retrieve'),
# 	url(r'^(?P<pk>\d+)/update/$',StatusUpdateAPIView.as_view(),name='update'),
# 	url(r'^(?P<pk>\d+)/destroy/$',StatusDestroyAPIView.as_view(),name='destroy'),
]

app_name = 'comments-api'