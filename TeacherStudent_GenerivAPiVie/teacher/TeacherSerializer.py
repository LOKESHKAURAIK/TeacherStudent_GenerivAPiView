from rest_framework import serializers
from .models import Teacher

class TeachSreializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'