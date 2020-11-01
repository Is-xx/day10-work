from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    gender_choices = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='pic', default='pic/1.jpg')
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    age = models.IntegerField()

    @property
    def user_info(self):
        return '这是用户：' + self.username

    @property
    def get_gender(self):
        return self.get_gender_display()

    @property
    def get_pic(self):
        return '%s%s%s' % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(self.pic))

    class Meta:
        db_table = 'user_table'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户：' + self.username
