from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Subreddit
from .models import Sentiment
from textblob import TextBlob
import requests
import pandas as pd

# Create your views here.

def index(request):

    if 'subreddit' in request.GET:
        nombre = request.GET['subreddit']
        try:
            getSubreddit(nombre)
        except KeyError:
            return redirect('error')

    page = request.GET.get('page', 1)
    subreddit = Subreddit.objects.all().order_by('-id')
    paginator = Paginator(subreddit, 4)
    lista = paginator.get_page(page)
    data = {
        'lista': lista,
        'paginator': paginator
    }

    return render(request, "subreddit/subreddit.html", data)


def eliminar_subr(request):
    try:
        subreddit_d = Subreddit.objects.all()
        sent = Sentiment.objects.all()
    except Subreddit.DoesNotExist:
        messages.error(request, "No existe ningún subreddit que eliminar")
        return redirect("subreddit")

    if subreddit_d:
        subreddit_d.delete()
        sent.delete()
        messages.error(request, 'Se han eliminado correctamente los subreddits')

    return redirect("subreddit")


def subirDrive(request):
    
    if Subreddit.objects.exists:
        return redirect("listar_drive")
    else:
        messages.error(request, 'No hay nada que subir')


def getSubreddit(name):

    client_id = 'VIbJ_oKFFSJuXkfDJvrURA'
    client_secret = 'uHKTFlc3ZXTzfGVAoiRs0dYXN8OSBA'

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    data = {
        'grant_type': 'password',
        'username': 'roy_dev',
        'password': 'practica_pi'
    }
    headers = {'User-Agent': 'MiAPI/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', 
                        auth=auth, data=data, headers=headers)
    
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'

    res = requests.get('https://oauth.reddit.com/r/'+name +'/new', 
                headers=headers, params={'limit': '5'})

    df2 = pd.DataFrame()
    for post in res.json()['data']['children']:
            
        df = pd.DataFrame({
            'subreddit': [post['data']['subreddit']],
            'title': [post['data']['title']],
            'selftext': [post['data']['selftext']],
            'upvote_ratio': [post['data']['upvote_ratio']],
            'ups': [post['data']['ups']],
            'downs': [post['data']['downs']],
            'score': [post['data']['score']]
            })
        df2 = pd.concat([df2, df], ignore_index=True)
        
    contexto = analisis(df2)

    df2['sent'] = contexto['dat']
    df2['contSubj'] = contexto['contSub']
    df2['contObj'] = contexto['contObj']
    
    insertar_datos(df2)

def insertar_datos(df):
    
    for index,row in df.iterrows():
        subr = Subreddit.objects.create(
                subreddit=row["subreddit"],
                title=row["title"],
                selftext=row["selftext"],
                upvote_ratio=row["upvote_ratio"],
                ups=row["ups"],
                downs=row["downs"],
                score=row["score"],
                sent=row["sent"],
                contSubj=row["contSubj"],
                contObj=row["contObj"]
                )
        subr.save()
        

def analisis(df):
    
    sent = 0
    subjectivity = 0
    objectivity = 0
    datos = []

    for index,row in df.iterrows():
        blob = TextBlob(row['selftext'])
        for sentence in blob.sentences:
            if sentence.sentiment.subjectivity > sent:
                sent = sentence.sentiment.subjectivity

        if sent >= 0.5:
            subjectivity = subjectivity+1
            datos = datos+['subjectivity']
        else:
            objectivity = objectivity+1
            datos = datos+['objectivity']

    context = {
        'dat' : datos,
        'contSub': subjectivity,
        'contObj': objectivity
    }
    
    return context


def get_chart(request):
    
    data = []
    subr = Subreddit.objects.first()
    data = data+[subr.contSubj]
    data = data+[subr.contObj]
    chart = {
        'title':[
            {
                'text': 'Análisis Sentimiento',
                'subtext': 'subreddits',
                'left': 'center'
            }
        ],
        'tooltip': [
            {
                'trigger': "item"
            }
        ],
        'legend': [
            {
                'orient': 'vertical',
                'left': 'left'
            }
        ],
        'series':[
            {
                'name': 'Access From',
                'type': 'pie',
                'radius': '50%',
                'data': [
                    { 'value': data[0], 'name': 'Subjectivity'},
                    { 'value': data[1], 'name': 'Objectivity'}
                ]
            }
        ]
    }

    return JsonResponse(chart)