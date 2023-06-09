from django.urls import path, include
from . import views

urlpatterns = [
 path('motech/', views.motech, name="motech"),
 path('form/', views.uploadForm, name='form'),
 path('upload/', views.uploadFile, name='upload'),
 path('files/', views.FileView.as_view(), name='files'),
 path('pelcon/', views.PelconView.as_view(), name='pelcon'),
 path('myupload/', views.myUpload, name='myupload'),
 path('pelconUpload/', views.pelconUpload, name='pelconUpload'),


]
