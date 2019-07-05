from django.db import models

# Create your models here.

# 首页文章表
class Tags(models.Model):
    tag_id = models.CharField(max_length=20)
    tag_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Learn_tags'
