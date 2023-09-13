import requests
from django.shortcuts import render
import datetime
import pandas as pd
from django.utils.safestring import mark_safe
from googledrive.views import subir_archivo_drive


df = pd.DataFrame(columns=['Usuario', 'Karma', 'Karma_links', 'Karma_comentarios', 'Subreddit_principal', 'Karma_logros', 'Fecha_creacion', 'Fecha_busqueda'])


def formulario(request):

    return render(request, 'search_user/reddit_form.html')

def user_info(request):
    global df

    if 'nickname' in request.GET:
        # Obtén el nickname del usuario desde los parámetros de la URL
        nickname = request.GET.get('nickname')

        # Realiza la solicitud GET a la API de Reddit
        url = f'https://www.reddit.com/user/{nickname}/about.json'
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

        if response.status_code == 200:
            # Extrae la información del usuario de la respuesta JSON
            data = response.json()['data']
            # Accede a los campos deseados, por ejemplo:
            username = data.get('name', 'No se ha encontrado un username para este usuario.')
            subreddit_principal = data.get('title', 'Este usuario no tiene un subreddit principal.')
            karma_links = data.get('link_karma', 'Este usuario no tiene karma por links.')
            karma_comments = data.get('comment_karma', 'Este usuario no tiene karma por comentarios.')
            karma_awardee = data.get('awardee_karma', 'Este usuario no tiene karma por logros')
            karma_total = data.get('total_karma', 'Este usuario no tiene karma.')
            snoovatar_img = data.get('snoovatar_img', 'Este usuario no tiene configurado un snoovatar o no lo tiene público.')
            fecha_creacion = data.get('created_utc', 'No existe fecha de creación o no este usuario no la tiene pública.') 
           
            # Crea un objeto datetime a partir del valor en UTC
            datetime_utc = datetime.datetime.utcfromtimestamp(fecha_creacion)  
            # Aplica la conversión a la zona horaria de Madrid
            timezone_madrid = datetime.timezone(datetime.timedelta(hours=2))  # UTC+2 para Madrid
            datetime_madrid = datetime_utc.replace(tzinfo=datetime.timezone.utc).astimezone(timezone_madrid)
            # Formatea la fecha y hora en el formato deseado
            fecha_creacion = datetime_madrid.strftime('%d-%m-%Y %H:%M:%S')
            fecha_busqueda = datetime.datetime.now().strftime('%H:%M:%S')

            # Crea un DataFrame con los datos del usuario
            data_dict = {
            'Usuario': [username],
            'Karma': [karma_total],
            'Karma_links': [karma_links],
            'Karma_comentarios': [karma_comments],
            'Subreddit_principal': [subreddit_principal],
            'Karma_logros': [karma_awardee],
            'Fecha_creacion': [fecha_creacion],
            'Fecha_busqueda': [fecha_busqueda]
            }
            # Agrega una nueva fila al Dataframe global
            new_df = pd.DataFrame(data_dict)
            df = pd.concat([df, new_df], ignore_index=True)

        
            # Renderiza un template con los datos obtenidos
            return render(request, 'search_user/reddit_info.html', {'nickname': username, 'subreddit_principal': subreddit_principal,'karma_logros': karma_awardee,'karma_links': karma_links,'karma_comentarios': karma_comments,'karma': karma_total, 'icono_snoovatar': snoovatar_img, 'fecha_creacion': fecha_creacion})
    # Maneja posibles errores
    error_message = 'Error al obtener la información del usuario Reddit.'
    return render(request, '/workspace/reddit_app/inicio/templates/inicio/error.html', {'error_message': error_message})


def tabla_usuarios(request):
    # Renderiza un template con la tabla de usuarios
    global df
    html_table = df.to_html(index=False, classes='table custom-table', border = 0, justify='center')

    html_table = html_table.replace('<th', '<th style="border: 2px solid black; padding: 8px;"')
    html_table = html_table.replace('<td', '<td style="border: 2px solid black; padding: 8px;"')


    return render(request, 'search_user/tabla_usuarios.html', {'html_table': html_table})



def eliminar_tabla(request):
    global df
    df = pd.DataFrame(columns=['Usuario', 'Karma', 'Karma_links', 'Karma_comentarios', 'Subreddit_principal', 'Karma_logros', 'Fecha_creacion', 'Fecha_busqueda'])
    return render(request, 'search_user/tabla_usuarios.html')



def subir_tabla(request):
    global df
    if df.empty:
        return render(request, 'inicio/error.html', {'error_message': 'No hay datos en la tabla a subir.'})

    # Obtener la tabla HTML
    html_table = df.to_html(index=False, classes='table table-striped')

    # Generar el archivo CSV
    csv_data = df.to_csv(index=False)

    # Guardar el archivo CSV en el servidor
    archivo_csv = 'tabla_usuarios.csv'
    with open(archivo_csv, 'w') as file:
        file.write(csv_data)

    # Subir el archivo CSV a Google Drive
    carpeta_id = '1fQ6BmrDjBp0pGn19_U6tebNbtgS7SHKh'

    # Eliminar la tabla del DataFrame
    df = pd.DataFrame(columns=['Usuario', 'Karma', 'Karma_links', 'Karma_comentarios', 'Subreddit_principal', 'Karma_logros', 'Fecha_creacion', 'Fecha_busqueda'])
    

    return render(request, 'search_user/subir_tabla.html', {'html_table': mark_safe(html_table), 'carpeta_id': carpeta_id, 'archivo_csv': archivo_csv})


