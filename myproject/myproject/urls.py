# /share/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from Share.views import HomeView,DisplayView,SearchView,MyView
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name="home"),
    url(r'^s/(?P<code>\d+)/$',DisplayView.as_view()),
    url(r'^search/',SearchView.as_view(),name="search"), #添加的路由
    url(r'^my/$',MyView.as_view(),name="MY")
]