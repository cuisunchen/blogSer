from rest_framework import serializers
from .models import Tags

class TagsSerializer(serializers.Serializer):
    tag_id = serializers.CharField()
    tag_name = serializers.CharField()




