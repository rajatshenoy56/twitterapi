from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView
    )

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)

from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer,
	UserListSerializer,
	UserRetrieveSerializer
    )
from django.contrib.auth.models import User
from accounts.models import UserFollowing

from .permissions import isLoggedIn

class UserListAPIView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserListSerializer
	permission_classes = [IsAuthenticated, ]

class UserRetrieveAPIView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserRetrieveSerializer
	permission_classes = [IsAuthenticated,]

class UserCreateAPIView(CreateAPIView):
	permission_classes = [isLoggedIn]
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
	permission_classes = [isLoggedIn]
	serializer_class = UserLoginSerializer

	def post(self,request, *args, **kwargs):
		data = request.data	
		serializer= UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception = True):
			new_data = serializer.data
			return Response(new_data, status= HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class FollowView(viewsets.ViewSet):
	queryset = UserFollowing.objects
	permission_classes = [IsAuthenticated]
	def follow(self, request, pk):
		print(pk)
		print(request.user.id)
		if int(pk) == int(request.user.id):
			return Response({'message': 'Cant follow yourself'}, status=HTTP_400_BAD_REQUEST)
		else:
			UserFollowing.objects.create(following = User.objects.get(id= pk), follower = request.user)
			return Response({'message': 'Followed'}, status=HTTP_200_OK)

    