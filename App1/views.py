from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

def thankyou(request):
    templates = loader.get_template('thankyou.html')
    return HttpResponse((templates.render()))

def content(request):
    templates = loader.get_template('content.html')
    return HttpResponse((templates.render()))

def crowd(request):
    templates = loader.get_template('crowd.html')
    return HttpResponse((templates.render()))

def graphic(request):
    templates = loader.get_template('graphic.html')
    return HttpResponse((templates.render()))

def Home(request):
    templates = loader.get_template('Home.html')
    return HttpResponse((templates.render()))

def post(request):
    templates = loader.get_template('post.html')
    return HttpResponse((templates.render()))


def translate(request):
    templates = loader.get_template('translate.html')
    return HttpResponse((templates.render()))

def work(request):
    templates = loader.get_template('work.html')
    return HttpResponse((templates.render()))

def write(request):
    templates = loader.get_template('write.html')
    return HttpResponse((templates.render()))

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            return redirect('Home.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')