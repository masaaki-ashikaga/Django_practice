from django.urls import path
from .views import TodoList, TodoDetail
from .views import TodoList, TodoCreate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
]
