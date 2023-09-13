from django.shortcuts import render
import requests
import pandas as pd
from textblob import TextBlob
import praw


def index(request):
    # Inicializar la instancia de Reddit
    reddit = praw.Reddit(
        client_id='TU_CLIENT_ID',
        client_secret='TU_CLIENT_SECRET',
        user_agent='NombreDeTuApp/v1.0 (por /u/TuNombreDeUsuario)'
    )
    

    subreddits_list = [
        "WorldNews",
        "AskHistory",
        "LeagueOfLegends",
        "DogeCoin",
        "UFC",
        "Games",
        "Comics",
        "Fortnite",
        "Movies",
        "LGBT",
        "Spain",


    ]
    
    subreddits = []
    
    for country in subreddits_list:
        subreddit = reddit.subreddit(country)
        subreddits.append(subreddit.display_name)
    
    # Renderizar la plantilla con la lista de subreddits
    context = {'subreddits': subreddits}
    return render(request, 'textblob_comments/home.html', context)


def getComment(request, subreddit):
    reddit = praw.Reddit(client_id='VIbJ_oKFFSJuXkfDJvrURA',
                        client_secret='uHKTFlc3ZXTzfGVAoiRs0dYXN8OSBA',
                        user_agent='AgentePracticaPI')


    subreddit_search = reddit.subreddit(subreddit)
    posts = subreddit_search.new(limit=1)

    post = next(posts, None)  # Obtener el primer post o None si no hay posts

    if post:
        post_title = post.title
        post_body = post.selftext

        body_sentiment = TextBlob(post.selftext).sentiment.polarity


        title_sentiment = TextBlob(post.title).sentiment.polarity

        average_sentiment = (title_sentiment + body_sentiment) / 2

        
        # Determinar si la media es positiva o negativa
        if average_sentiment > 0:
            sentiment_label = "Positivo"
        elif average_sentiment < 0:
            sentiment_label = "Negativo"
        else:
            sentiment_label = "Neutral"

       
        return render(request, 'textblob_comments/comment.html', {'post_title': post_title, 'post_body': post_body, 'sentiment': sentiment_label, 'average': average_sentiment})
    else:
        return render(request, 'textblob_comments/comment.html', {'error_message': 'No se encontró ningún post'})
    