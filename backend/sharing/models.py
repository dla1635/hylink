from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from ..links.models import Link

class Share(models.Model):
    title = models.CharField(max_length=144, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class ShareLink(models.Model):
    class Meta:
        unique_together = (('share', 'order'),)
    
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='sharelink')
    order = models.IntegerField(default=0)
