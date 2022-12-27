from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
]
