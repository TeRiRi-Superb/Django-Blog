from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogUser(User):

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'B_User'
        verbose_name = '用户'
        verbose_name_plural = verbose_name