from django.db import models
from django.contrib.auth.models import User
from  status.models import Status

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
    parent = models.ForeignKey(Status,on_delete=models.CASCADE,default=1)
    content = models.TextField()