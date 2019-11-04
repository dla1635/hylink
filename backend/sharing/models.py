from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ..links.models import Link

class Share(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class LinkGroup(models.Model):
    group = models.ForeignKey(Share, related_name='sharing', on_delete=models.CASCADE)
    link = models.ForeignKey(Link, related_name='share_link', on_delete=models.CASCADE)