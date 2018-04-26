#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['keyword1'] = '你好!'
    context['k2'] = '大家好!'
    context['k3'] = '大家好!'
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello world ! ")