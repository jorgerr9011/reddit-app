from django.shortcuts import render, redirect
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.files import FileNotUploadedError
from django.contrib import messages
import pandas as pd
import json
import pytz

# Create your views here.

def index(request):
    datos = listar_elementos_carpeta(request, '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh')
    
    if datos.empty == True:
        data = []
    else:
        # Convertir 'createdDate' a tipo datetime
        datos['createdDate'] = pd.to_datetime(datos['createdDate'])
        
        # Convertir la hora a horario de Madrid
        madrid_timezone = pytz.timezone('Europe/Madrid')
        datos['createdDate'] = datos['createdDate'].dt.tz_convert(madrid_timezone)
        
        # Formatear la hora en horario de Madrid
        datos['createdDate'] = datos['createdDate'].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        json_records = datos.reset_index().to_json(orient='records')
        data = json.loads(json_records)
    
    context = {'dat': data}
    
    return render(request, 'listardrive/index.html', context)





directorio_credenciales = 'googledrive/credentials_module.json'


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


def listar_elementos_carpeta(request, carpeta_id):
    credenciales = login()

    items = credenciales.ListFile({'q': f"'{carpeta_id}' in parents and trashed=false"}).GetList()

    if not items:
        df2 = pd.DataFrame()
        messages.error(request, 'No hay ningún archivo subido')

        return df2
    else:
        df2 = pd.DataFrame()
        for item in items:
            df = pd.DataFrame({
                'titulo': [item["title"]],
                'nId': [item["id"]],
                'fileExtension': [item["fileExtension"]],
                'createdDate': [item["createdDate"]],
                'fileSize': [item["fileSize"]],
            })
            df2 = pd.concat([df2, df], ignore_index=True)
        return df2


def eliminar_archivo(request):
    credenciales = login()

    if(request.method=='POST'):
        id_archivo = request.POST.get('nId')
        archivo = credenciales.CreateFile({'id': id_archivo})
        archivo.Delete()
        messages.error(request, 'Se ha eliminado correctamente el archivo')

    return redirect("listar_drive")


def eliminar_drive(request):
    carpeta_id = '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh'
    credenciales = login()
    
    items = credenciales.ListFile({'q': f"'{carpeta_id}' in parents and trashed=false"}).GetList()

    if not items:
        messages.error('No hay elementos que borrar en la carpeta')
        return redirect('listar_drive')
    else:
        for item in items:
            archivo = credenciales.CreateFile({'id': item['id']})
            archivo.Delete()

        messages.error(request, 'Se han eliminado correctamente los elementos')
        return redirect('listar_drive')