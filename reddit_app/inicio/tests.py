from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .views import index

class IndexViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        # Realizar una solicitud GET a la vista index
        response = self.client.get(reverse('index'))

        # Comprobar el código de estado de la respuesta
        self.assertEqual(response.status_code, 200)

        # Comprobar que el usuario está en el contexto de la respuesta
        self.assertEqual(response.context['user'], user)

        # Comprobar que el formulario de registro está en el contexto de la respuesta
        self.assertIn('signup_form', response.context)
