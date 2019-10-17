from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE = 삭제시 foreignkey를 포함하는 모델 인스턴스도 삭제
    title = models.CharField(max_length=144)
    contents = models.TextField(blank=True) # 빈칸 가능 
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    
    # admin 페이지에서 보여줄 내용 
    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.title)