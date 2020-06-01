from rest_framework.serializers import EmailField,CharField,ModelSerializer,HyperlinkedIdentityField
from status.models import Status
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [  
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {"password": {"write_only":True}}

    def validate_email(self,value):
        email = value
        user = User.objects.filter(email = email)
        if user.exists():
            raise ValidationError("The useremail has already registered")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [  
            'email',
            'password',
        ]
        extra_kwargs = {"password": {"write_only":True}}

    def validate(self,data):
        user_ = None
        email = data["email"]
        password = data["password"]
        temp_user = User.objects.filter(email = email)

        if temp_user.exists():
            user = temp_user.first()
        else:
            raise ValidationError("This email is not valid")
        
        if user:
            if not user.check_password(password):
                raise ValidationError("Incorrect password")

        return data

class UserListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = "accounts-api:retrieve"
    )
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
        ]

class UserRetrieveSerializer(ModelSerializer):
    follow_link = HyperlinkedIdentityField(
        view_name = "accounts-api:follow"
    )
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'follow_link'
        ]