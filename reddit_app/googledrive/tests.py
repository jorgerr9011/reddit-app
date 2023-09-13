from django.test import TestCase
from django.urls import reverse

class SubirArchivoDriveTestCase(TestCase):
    def test_subir_archivo_drive(self):
        url = reverse('googledrive')
        response = self.client.post(url, {
            'archivo_csv': 'tabla_usuarios.csv',
            'nombre_archivo': 'tabla_usuarios.csv',
            'carpeta_id': '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'googledrive/subido.html')
        

class SubirSubredditTestCase(TestCase):
    def test_subir_subreddit(self):
        url = reverse('subir_subr')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'googledrive/subir_subr.html')
        
class SubirRedditsTestCase(TestCase):
    def test_subir_reddits(self):
        url = reverse('subir_reddits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_user/subir_tabla.html')
        




