from rest_framework import serializers

from livros.models import Livros


class LivrariaSerializer(serializers.ModelSerializer):
    
    class Meta:
         model = Livros
         fields = '__all__'