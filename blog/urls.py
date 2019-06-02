from django.urls import path
from . import views#views.py znotraj blog aplikacije
urlpatterns = [
    path('', views.allblog, name='blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]
