from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE,default=1)
	text = models.TextField()
	n_likes = models.IntegerField(default=0)
	n_shares = models.IntegerField(default=0)
	n_comments = models.IntegerField(default=0)
	