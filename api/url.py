from django.urls import path
from .views import AddTask


urlpatterns = [
    # path('task/', TaskView.as_view()),
    # path('task/<int:pk>/', TaskView.as_view()),
    path('add/',AddTask.as_view())
]