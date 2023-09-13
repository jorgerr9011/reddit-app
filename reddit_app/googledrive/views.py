from django.shortcuts import render
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from subreddit.models import Subreddit
import pandas as pd

# Create your views here.
directorio_credenciales = 'googledrive/credentials_module.json'


# Función para subir un archivo a Google Drive
def subir_archivo_drive(request):
    if request.method == 'POST':
        ruta_archivo = request.POST.get('archivo_csv')
        nombre_archivo = request.POST.get('nombre_archivo')
        id_folder = request.POST.get('carpeta_id')
        credenciales = login()
        
        archivo = credenciales.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                        "id": id_folder}]})
        archivo['title'] = nombre_archivo
        archivo.SetContentFile(ruta_archivo)
        archivo.Upload()
        file_id = archivo.get('id')

    return render(request, 'googledrive/subido.html', {'file_id': file_id})


# INICIAR SESION
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8090])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales


def subir_subreddit(request):
    subr = Subreddit.objects.all()

    df = pd.DataFrame()
    df = crear_dataframe()

    csv_data = df.to_csv(index=False)

    archivo_csv = 'tabla_subreddits.csv'
    with open(archivo_csv, 'w') as file:
        file.write(csv_data)

    carpeta_id = '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh'

    context = {
        'subreddits': subr,
        'carpeta_id': carpeta_id,
        'archivo_csv': archivo_csv
    }

    return render(request, 'googledrive/subir_subr.html', context)


def subir_Reddits(request):
    
    df = crear_dataframe()

    # Generar el archivo CSV
    csv_data = df.to_csv(index=False)

    # Guardar el archivo CSV en el servidor
    archivo_csv = 'tabla_subreddits.csv'
    with open(archivo_csv, 'w') as file:
        file.write(csv_data)

    # Subir el archivo CSV a Google Drive
    carpeta_id = '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh'
    

    return render(request, 'search_user/subir_tabla.html', {'carpeta_id': carpeta_id, 'archivo_csv': archivo_csv})


def crear_dataframe():
    subr = Subreddit.objects.all()

    df2 = pd.DataFrame()
    for sub in subr:
        df = pd.DataFrame({
            'subreddit': [sub.subreddit],
            'title': [sub.title],
            'selftext': [sub.selftext],
            'upvote_ratio': [sub.upvote_ratio],
            'ups': [sub.ups],
            'downs': [sub.downs],
            'score': [sub.score],
            'sent': [sub.sent]
            })
        df2 = pd.concat([df2, df], ignore_index=True)

    return df2

 

# CREAR CARPETA
def crear_carpeta(nombre_carpeta,id_folder):
    credenciales = login()
    folder = credenciales.CreateFile({'title': nombre_carpeta, 
                               'mimeType': 'application/vnd.google-apps.folder',
                               'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    folder.Upload()


