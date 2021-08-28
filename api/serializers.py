from rest_framework import serializers
from api.models import Categories


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'page']
