from django.urls import path, include
from ChampionsLeague import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.players, name='player'),
    path('teams/', views.teams, name='teams'),
    path('top_scorer/', views.top_scorer, name='top_scorer'),
    path('managers/', views.managers, name='managers'),
    path('mvp/', views.mvp, name='mvp'),
    path('mvt/', views.mvt, name='mvt'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
