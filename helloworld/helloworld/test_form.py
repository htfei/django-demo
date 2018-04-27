# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf

# 表单
def testForm(request):
    # 在url中进行绑定，http://127.0.0.1:8000/search-form
    return render_to_response('testForm.html')
 
# 接收请求数据
def search(request):  
    # 在url中进行绑定，http://127.0.0.1:8000/search or http://127.0.0.1:8000/search?q=y
    request.encoding='utf-8'
    if 'q' in request.GET: # request.GET即请求url中的参数
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    # 测试post需要使用 http://127.0.0.1:8000/search-post 
    # 而非  http://127.0.0.1:8000/testForm ，即使2者绑定的同一个html模版
    # 猜测原因：render_to_response 和 render 区别
    # ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q2']
    return render(request, "testForm.html", ctx)