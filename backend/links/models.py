from django.db import models
from django.conf import settings

class Link(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    url = models.TextField()
    title = models.CharField(max_length=144, blank=True)
    thumbnail = models.TextField(blank=True)
    summary = models.TextField()
    sharable = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField('Tag', through='LinkTag', blank=True)
    label = models.ManyToManyField('Label', through='LinkLabel', blank=True)
    
    def __str__(self):
        return '[{}] {}'.format(self.user.nickname, self.title)


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LinkTag(models.Model):
    link = models.ForeignKey(Link, related_name='link_tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='link_tags', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} & {} | {}".format(self.link.title, self.tag.name, self.date_joined)

class LinkLabel(models.Model):
    link = models.ForeignKey(Link, related_name='link_labels', on_delete=models.CASCADE)
    label = models.ForeignKey(Label, related_name='link_labels', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} & {} | {}".format(self.link.title, self.label.name, self.date_joined)