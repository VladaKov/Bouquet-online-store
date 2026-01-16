from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home/', views.startHome, name='start_home'),  # ← Убедитесь, что есть name
]