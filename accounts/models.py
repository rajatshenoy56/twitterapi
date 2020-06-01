from django.db import models
from django.contrib.auth.models import User
from status.models import Status
# Create your models here.
class UserFollowing(models.Model):
    following = models.ForeignKey(User, on_delete = models.CASCADE, related_name="following")
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name="follower")

class UserLikes(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, default =1)
    status = models.ForeignKey(Status, on_delete = models.CASCADE,default=1)