import os
import django
import sys

# Adiciona o diretório que contém manage.py ao path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()