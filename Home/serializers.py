from rest_framework import serializers
from .models import Articles

class NavSerializer(serializers.Serializer):
    nav_name = serializers.CharField()
    nav_eng = serializers.CharField()
    nav_pageUrl = serializers.CharField()

class ArtSerializer(serializers.Serializer):
    tagId = serializers.CharField()
    title = serializers.CharField()
    imgIndex = serializers.IntegerField()
    text = serializers.CharField()
    date = serializers.DateField()
    time = serializers.TimeField()

class TagSerializer(serializers.Serializer):
    tag_id = serializers.CharField()
    tag_name = serializers.CharField()




