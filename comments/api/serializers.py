from rest_framework.serializers import ModelSerializer,SerializerMethodField,HyperlinkedIdentityField

from comments.models import Comment

class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'user',
            'content',
            'parent'
        ]
    def get_user(self, obj):
        return str(obj.user.username)
        
class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]