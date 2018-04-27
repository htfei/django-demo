#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # 类代表视图的名称，在url中进行绑定，此类绑定的url为“http://127.0.0.1:8000/hello”
    context = {}
    context['keyword1'] = '你好!'
    context['k2'] = '大家好!'
    context['k3'] = '大家好!'
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello world ! ")