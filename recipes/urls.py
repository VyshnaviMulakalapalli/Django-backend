from django.urls import path
from . import views

urlpatterns = [
    path('api/recipes/', views.RecipeListCreate.as_view(), name='recipe-list-create'),
    path('api/add_recipe/', views.RecipeListCreate.as_view(), name='add-recipe'),
    path('api/update_recipe/<int:pk>/', views.RecipeUpdate.as_view(), name='update-recipe'),
]