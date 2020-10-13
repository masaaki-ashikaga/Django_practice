from django.urls import path
from .views import TodoList, TodoDetail
from .views import TodoList, TodoCreate

urlpatterns = [
    path('list/', TodoList.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view()),
    path('create/', TodoCreate.as_view()),
]
