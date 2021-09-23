from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),

    path('tags-page', views.tagsPage, name='tags-page'),
    path('tags-filter/<str:tagName>/', views.tagsFilter, name='tags-filter'),
]