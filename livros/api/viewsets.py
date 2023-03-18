from rest_framework import viewsets

from livros.api.serializers import LivrariaSerializer
from livros.models import Livros


class LivrosViewSets(viewsets.ModelViewSet):
    
    serializer_class = LivrariaSerializer
    queryset = Livros.objects.all()

    
    
    
    #http://127.0.0.1:8000/livros/?autor=diogo
    def get_queryset(self):
        autor = self.request.query_params.get('autor', None)
        
        #http://127.0.0.1:8000/livros/?autor=diogo&?titulo=O condenado
        titulo = self.request.query_params.get('titulo', None)
        
        queryset = Livros.objects.all()
        
        if autor:
            queryset = queryset.filter(autor__icontains=autor)
        
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        
        return queryset