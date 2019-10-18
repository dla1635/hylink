from django.db import models
from django.conf import settings

class Link(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    url = models.TextField()
    title = models.CharField(max_length=45, blank=True)
    thumbnail = models.TextField(blank=True)
    summary = models.TextField()
    sharable = models.IntegerField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '[{}] {}'.format(self.user.nickname, self.title)


class Tag(models.Model):
    name = models.CharField(max_length=45)
    links = models.ManyToManyField('Link', through='LinkTagJoin', related_name='tags')

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=45)
    links = models.ManyToManyField('Link', through='LinkLabelJoin', related_name='labels')

    def __str__(self):
        return self.name


class LinkTagJoin(models.Model):
    link = models.ForeignKey(Link, related_name='link_from_tag', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag_from_link', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} & {} | {}".format(self.link.title, self.tag.name, self.date_joined)

class LinkLabelJoin(models.Model):
    link = models.ForeignKey(Link, related_name='link_from_label', on_delete=models.CASCADE)
    label = models.ForeignKey(Label, related_name='label_from_link', on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} & {} | {}".format(self.link.title, self.label.name, self.date_joined)