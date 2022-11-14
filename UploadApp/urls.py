from django.urls import path,include
from . import views
urlpatterns = [
path('UploadImage', views.UploadImage, name='UploadImage'),
]
