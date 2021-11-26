from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题', help_text='言简意赅的表述大意即可')
    content = models.TextField(verbose_name='内容', help_text='重要的细节及逻辑')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(default='flash_pics/default.jpg',
                                upload_to='flash_pics',
                                blank=True)
    def __str__(self):
        return self.post.title
