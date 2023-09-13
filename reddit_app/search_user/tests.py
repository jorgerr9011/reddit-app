import pytest
from django.urls import reverse
from django.test import Client
from .models import User

@pytest.fixture
def client():
    return Client()

def test_formulario(client):
    response = client.get(reverse('reddit_form'))
    assert response.status_code == 200
    assert 'Búsqueda de usuario de Reddit' in response.content.decode('utf-8')

def test_user_info_success(client):
    response = client.get(reverse('reddit_info'), {'nickname': 'example'})
    assert response.status_code == 200
    assert 'Información de Reddit para el usuario: example' in response.content.decode('utf-8')
    # Se asegura de que todos los campos estén en la respuesta
    assert 'Karma por links' in response.content.decode('utf-8')
    assert 'Karma por comentarios' in response.content.decode('utf-8')
    assert 'Karma por logros' in response.content.decode('utf-8')
    assert 'Karma total' in response.content.decode('utf-8')
    assert 'Subreddit principal del usuario' in response.content.decode('utf-8')
    assert 'Cake day' in response.content.decode('utf-8')

def test_user_info_error(client):
    response = client.get(reverse('reddit_info'))
    assert response.status_code == 200
    assert 'Error al obtener la información de Reddit.' in response.content.decode('utf-8')

def test_tabla_usuarios(client):
    response = client.get(reverse('tabla_usuarios'))
    assert response.status_code == 200
    assert 'Tabla de Usuarios' in response.content.decode('utf-8')
    # Se asegura de que la tabla de usuarios se encuentre en la respuesta
    assert '<table' in response.content.decode('utf-8')

def test_eliminar_tabla(client):
    response = client.post(reverse('eliminar_tabla'))
    assert response.status_code == 200
    assert 'Tabla de Usuarios' in response.content.decode('utf-8')
    # Se asegura de que la tabla de usuarios esté vacía en la respuesta
    assert '<table' not in response.content.decode('utf-8')

def test_subir_tabla(client):
    response = client.get(reverse('subir_tabla'))
    assert response.status_code == 200
    assert 'Tabla a Subir' in response.content.decode('utf-8')
    # Se asegura de que el formulario para subir a Google Drive se encuentre en la respuesta
    assert '<form' in response.content.decode('utf-8')
    assert 'action="{% url \'googledrive\' %}"' in response.content.decode('utf-8')

