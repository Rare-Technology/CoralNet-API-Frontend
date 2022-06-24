from django.urls import path
from . import views

app_name = 'coralnet'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dropbox/', views.dropbox_view, name = 'dropbox')
]
