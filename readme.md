
# API Livraria com Django Rest Framework
Há como objetivo gerenciar informações sobre livros 
como título, autor, ano de lançamento, status, número de páginas e data de criação.Com a API Livraria é possível obter, adicionar, editar e deletar um livro. Além disso, também é possível realizar busca pelos autores.

O desenvolvedor pode encontrar toda a documentação referente à API
na página /api/docs/. A documentação da API foi criada com Swagger e
está disponível em Português, para facilitar o entendimento e utilização dos endpoints.

<br>

# Configuração do ambiente:
```bash
 py -m venv venv
 .\venv\scripts\activate    
 pip install -r requirements.txt
 py manage.py makemigrations
 py manage.py migrate
 py manage.py runserver
```

<br>

