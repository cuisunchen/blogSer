from django.db import models

# Create your models here.

# nav表
class Navs(models.Model):
    nav_name = models.CharField(max_length=20)
    nav_eng = models.CharField(max_length=20)
    nav_pageUrl = models.CharField(db_column='nav_pageUrl', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'navs'


# 首页文章表
class Articles(models.Model):
    tagId = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    imgIndex = models.IntegerField(db_column='imgIndex')  # Field name made lowercase.
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'Home_articles'


