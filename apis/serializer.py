# serializers.py
from rest_framework import serializers
from .models import Therapist

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'  # Serialize all fields
        # Or you can specify fields explicitly:
        # fields = ['id', 'name', 'age', 'gender', 'expertise', 'language', 'session_type', 'availability', 'budget']
