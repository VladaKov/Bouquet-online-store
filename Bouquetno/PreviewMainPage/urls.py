from django.urls import path
from . import views

app_name = 'preview'

urlpatterns = [
    path('', views.start, name='preview_page'),
]