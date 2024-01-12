from django.contrib import admin
from django.urls import path,re_path
# from django.conf.urls import url
from ScriptStudio import views

urlpatterns = [
    re_path(r'^script$',views.scriptApi),
    re_path(r'^script$',views.scriptApi),
    re_path(r'^script/([0-9]+)$',views.scriptApi),
    re_path(r'^genscript$',views.generate),

    path('admin/', admin.site.urls),
]