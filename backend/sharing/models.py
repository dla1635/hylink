from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ..links.models import Link

class Share(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sharelink = models.ManyToManyField('ShareLink',related_name='share')

class ShareLink(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='sharelink')
    order = models.IntegerField(default=0)
