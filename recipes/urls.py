from ast import pattern
from recipes.views import home
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]