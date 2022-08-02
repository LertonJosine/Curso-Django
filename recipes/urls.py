from django.contrib import admin
from django.urls import path
from recipes.views import home, sobre, contacto
    

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('sobre/', sobre),
    path('contacto/', contacto)
]
