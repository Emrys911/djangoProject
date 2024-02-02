from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request): return HttpResponse('hello world')

def Mila(request):
    name = 'dex'
    return render(request,'asdf.html',{'name':name})

def reverse(request):
    test = request.Get['text']
    return render(request,'reverse.html',{"usertext":test})
def koko(request):
    if request.method == 'POST':
        return HttpResponse('post запрос обработан')

def momo(request):
    if request.method == 'GET':
     return HttpResponse('get запрос обработан')

@csrf_exempt
def ghjj(request):
 if request.method == 'DELETE':
     return HttpResponse('delete запрос обработан')
 return HttpResponse('GET')

