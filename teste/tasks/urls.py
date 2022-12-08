from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.taskList, name="task-list"),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('seunome/<str:nome>', views.seuNome, name="SN"),
]
