from django.urls import path
from regandloginapp import views
urlpatterns=[
path('input', views.input),
path('regestration', views.reg),
path('log', views.login),
]
