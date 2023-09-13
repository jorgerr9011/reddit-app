
"""myciao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('subreddit/', include('subreddit.urls')),
    path('search_user/', include('search_user.urls')),
    path('googlemaps/', include('googlemaps.urls')),
    path('googledrive/', include('googledrive.urls')),
    path('listardrive/', include('listardrive.urls')),
    path('comments/', include('textblob_comments.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Esto nos sirve para que salte nuestra pagina de error cuando se
#introduzca alguna url mal
handler404 = 'inicio.views.error_404_view'
handler500 = 'inicio.views.error500'
handler400 = 'inicio.views.error400'