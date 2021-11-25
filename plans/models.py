from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class PlanTag(models.Model):
    name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    plan_detail = models.CharField(max_length=200, verbose_name='名称', help_text='任务内容', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    plan_state = models.IntegerField(verbose_name='任务状态', default = 0, null=True)


    def __str__(self):
        return self.plan_detail

    def get_absolute_url(self):
        return reverse('plan-detail', kwargs = {'pk': self.pk})
