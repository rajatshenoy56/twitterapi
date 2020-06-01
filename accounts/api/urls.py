from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	UserListAPIView,
	UserRetrieveAPIView,
	FollowView
	)

urlpatterns = [
	url(r'^register/$',UserCreateAPIView.as_view(), name='register'),
	url(r'^login/$',UserLoginAPIView.as_view(), name='login'),
	url(r'^list',UserListAPIView.as_view(), name= 'list'),
	url(r'^(?P<pk>\d+)/$',UserRetrieveAPIView.as_view(),name='retrieve'),
	url(r'^follow/(?P<pk>\d+)/$',FollowView.as_view({'post':'follow'}), name='follow'),
]

app_name = 'accounts-api'