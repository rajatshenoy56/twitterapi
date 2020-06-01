from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView)

from .permissions import IsUser,IsFollowerOrUser

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)

from status.models import Status
from accounts.models import UserLikes
from .serializers import (
	StatusListSerializer,
	StatusListAllSerializer,
	StatusRetrieveSerializer,
	StatusCreateSerializer,
	StatusShareSerializer,
	StatusLikeSerializer
	)


class StatusListAPIView(ListAPIView):
	# queryset = Status.objects.all()
	def get_queryset(self, *args, **kwargs):
		queryset = Status.objects.filter(user=self.request.user)
		return queryset
	serializer_class = StatusListSerializer
	permission_classes = [IsAuthenticated, IsUser]

class StatusListAllAPIView(ListAPIView):
	# queryset = Status.objects.all()
	def get_queryset(self, *args, **kwargs):
		list1 = []
		b = self.request.user.follower.values()
		for i in b:
			list1.append(i['following_id'])
		queryset = Status.objects.filter(user_id__in = list1)
		return queryset
	serializer_class = StatusListAllSerializer
	permission_classes = [IsAuthenticated, ]

class StatusRetrieveAPIView(RetrieveAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusRetrieveSerializer
	permission_classes = [IsAuthenticated, IsFollowerOrUser]


class StatusDestroyAPIView(DestroyAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusRetrieveSerializer
	permission_classes = [IsAuthenticated, IsUser]

class StatusUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusCreateSerializer
	permission_classes = [IsAuthenticated, IsUser]

class StatusCreateAPIView(CreateAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self,serializer):
		serializer.save(user= self.request.user,)

class StatusShareAPIView(CreateAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusShareSerializer
	permission_classes = [IsFollowerOrUser]

	def perform_create(self, serializer):
		statusid = self.kwargs['pk']
		statuss = Status.objects.get(id = statusid)
		statuss.n_shares = statuss.n_shares+1
		statuss.save()
		serializer.save(user = self.request.user, text = Status.objects.get(id = statusid).text,)

class StatusLikeAPIView(CreateAPIView):
	queryset = UserLikes.objects.all()
	serializer_class = StatusLikeSerializer
	permission_classes = [IsFollowerOrUser]

	def perform_create(self, serializer):
		statusid = self.kwargs['pk']
		statuss = Status.objects.get(id = statusid)
		list1=[]
		qs = UserLikes.objects.filter(status = statuss).values()
		print("okkk")
		for i in qs:
			print('okkkkkkk')
			list1.append(i['user_id'])
		if self.request.user.id in list1:
			statuss.n_likes = statuss.n_likes-1
			statuss.save()
			UserLikes.objects.filter(status = statuss, user =self.request.user).delete()
		else:
			statuss.n_likes = statuss.n_likes+1
			statuss.save()
			serializer.save(user = self.request.user, status = Status.objects.get(id=statusid))