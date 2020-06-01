from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView)

from status.api.permissions import IsUser

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)

from comments.models import Comment
from status.models import Status

from .serializers import (
	CommentSerializer,
	CommentCreateSerializer
    )

class CommentListAPIView(ListAPIView):
	# queryset = Comment.objects.all()
	def get_queryset(self, *args, **kwargs):
		queryset = Comment.objects.all()
		return queryset
	serializer_class = CommentSerializer
	permission_classes = [IsAuthenticated, IsUser]


class CommentCreateAPIView(CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self,serializer):
		parent_id = self.kwargs['pk']
		statuss = Status.objects.get(id = parent_id)
		statuss.n_comments = statuss.n_comments +1
		statuss.save()
		serializer.save(user= self.request.user,parent = Status.objects.get(id = parent_id))
		