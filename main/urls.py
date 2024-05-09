from django.urls import path
from main import views


urlpatterns = [
    path('', views.menu, name="menu"),
    path('menu/game_on/', views.game_on, name="game_on"),
]
