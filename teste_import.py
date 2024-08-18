import os
import django

# Defina a variável de ambiente para o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')

# Configure o Django
django.setup()

# Tente importar os modelos
from core.models import Categoria, Autor, Livro
print("Importação bem-sucedida!")
