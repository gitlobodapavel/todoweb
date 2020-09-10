from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('remove/<int:pk>', views.remove_task, name='remove_task'),
    path('complete/<int:pk>', views.complete_task, name='complete_task'),
]