from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('clients/', views.clients, name='clients'),
    path('clients/<int:client_id>', views.client, name='client'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>', views.project, name='project'),
]