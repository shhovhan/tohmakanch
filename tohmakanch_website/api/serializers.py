from rest_framework import serializers
from bio.models import Biography
from writings.models import Writing


class BiographySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Biography
        fields = ('author_name', 'bio')

class WritingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Writing
        fields = ('id', 'title', 'text')


class FavouriteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True, source='writing.title')
    text = serializers.CharField(read_only=True, source='writing.text')
    
    class Meta:
        model = Writing
        fields = ('id', 'title', 'text')
