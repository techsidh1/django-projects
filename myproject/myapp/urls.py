from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('createtask/', views.create_task, name='create_task'),
    path('doneTask/<str:pk>/', views.done_task, name='done_task'),
    path('undoneTask/<str:pk>/', views.undone_task, name='undone_task'),
    path('editTask/<str:pk>', views.edit_task, name='edit_task' ),
    path('deleteTask/<str:pk>/', views.delete_task, name='delete_task')
]
