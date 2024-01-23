from django.urls import path

from . import views

app_name = "loader"

urlpatterns = [
    path('kaggle/', views.load_data, name='load_data'),
]
