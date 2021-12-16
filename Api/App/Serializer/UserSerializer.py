from rest_framework import serializers

from Api.models import CustomUser
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','password']