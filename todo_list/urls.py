

from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'todo_list'
urlpatterns = [
    # path('', views.index_view, name='index'),
    path('', views.TodoIndexListView.as_view(), name='index'),
    path('List/', views.TodoListView.as_view(), name='list'),
    path('done/', views.DoneTodoView.as_view(), name='done'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='detail'),

    ]

