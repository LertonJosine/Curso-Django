from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/home.html', context={
        'name': 'Lerton herminio Josine'
    })


def contacto(request):
    return render(request, 'temp.html')
