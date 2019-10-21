from django.db import models
# from django.contrib.auth.models import User 
from django.conf import settings
from backend.links.models import Link 

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # CASCADE = 삭제시 foreignkey를 포함하는 모델 인스턴스도 삭제
    title = models.CharField(max_length=255)
    contents = models.TextField(blank=True) # 빈칸 가능 
    links = models.ManyToManyField(Link, related_name='link_posts') # M:N 모델 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)

    class Meta:
        ordering = ['-created_at']
    
    # admin 페이지에서 보여줄 내용 
    def __str__(self):
        return '[{}] {}'.format(self.user.email, self.title)

class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '[{}] {}, {}'.format(self.user.nickname, self.post.title, self.contents)


class PostReport(models.Model):
    report_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='report_posts', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="report_list")
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '[{}] {}, {}'.format(self.report_user.nickname, self.post.title, self.contents)