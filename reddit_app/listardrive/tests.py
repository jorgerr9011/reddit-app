from django.test import TestCase, RequestFactory
from .views import index
from django.urls import reverse
from googledrive.views import subir_archivo_drive

# Create your tests here.
class GoogleDriveTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        url = reverse('googledrive')
        request = self.factory.post(url, {
            'archivo_csv': 'tabla_usuarios.csv',
            'nombre_archivo': 'tabla_usuarios.csv',
            'carpeta_id': '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh',
        })
        response = subir_archivo_drive(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
