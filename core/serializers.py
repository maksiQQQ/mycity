from rest_framework import serializers
from .models import Proposial

class ProposialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposial
        fields = ['id', 'title']

class ProposialCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposial
        fields = ['title', 'description']

class ProposialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposial
        fields = ['id', 'title', 'description', 'photo']