from rest_framework import serializers
from .models import *

class FooPostSerializer (serializers.ModelSerializer):

    class Meta:
        model = FooPost
        fields = '__all__'
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes_count'] = instance.get_likes_count()
        repr['dislikes_count'] = instance.get_dislikes_count()
        return repr