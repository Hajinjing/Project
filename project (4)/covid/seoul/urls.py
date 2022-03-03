from . import views
from django.urls import include, path

app_name='seoul'
urlpatterns = [
    path('chart/', views.chart, name = 'chart'),
]
