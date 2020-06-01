from rest_framework.serializers import ModelSerializer,SerializerMethodField,HyperlinkedIdentityField, HyperlinkedRelatedField

from status.models import Status
from comments.models import Comment 
from accounts.models import UserLikes
from comments.api.serializers import CommentSerializer

class StatusListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "status-api:retrieve"
    )
    user = SerializerMethodField()
    class Meta:
        model = Status
        fields = [
            'url',
            'user',
            'text',
            'n_likes',
            'n_comments',
            'n_shares'
        ]
    def get_user(self, obj):
        return str(obj.user.username)

class StatusListAllSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "status-api:retrieve"
    )
    user = SerializerMethodField()
    class Meta:
        model = Status
        fields = [
            'url',
            'user',
            'text',
            'n_likes',
            'n_comments',
            'n_shares'
        ]
    def get_user(self, obj):
        return str(obj.user.username)

class StatusRetrieveSerializer(ModelSerializer):
    user = SerializerMethodField()
    comments = SerializerMethodField()
    create_comment_post_link = HyperlinkedIdentityField(
        view_name = "comments-api:create"
    )
    share_status_link = HyperlinkedIdentityField(
        view_name = "status-api:share"
    )
    like_status_link = HyperlinkedIdentityField(
        view_name = "status-api:like"
    )
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'text',
            'n_likes',
            'n_comments',
            'n_shares',
            'comments',
            'create_comment_post_link',
            'share_status_link',
            'like_status_link'
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_comments(self,obj):
        queryset = Comment.objects.filter(parent = Status.objects.get(id=obj.id))
        comments = CommentSerializer(queryset,many=True).data
        return comments

class StatusCreateSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'text',
        ]

class StatusShareSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = [
        ]

class StatusLikeSerializer(ModelSerializer):
    class Meta:
        model = UserLikes
        fields = [
        ]