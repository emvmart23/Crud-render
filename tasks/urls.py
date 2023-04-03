from django.urls import path
from . import views
from .views import list_tasks, create_task, delete_task, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.list_tasks),
  path('new/', views.create_task, name='create_task'),
  path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
  path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='list_tasks.html'), name='list_tasks')
]