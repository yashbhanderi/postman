from django.urls import path
from . import views

urlpatterns = [
    path('set-categories/', views.set_categories, name='set-categories'),
    path('get-categories/', views.get_categories, name='get-categories')
]
