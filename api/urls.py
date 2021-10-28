from django.urls import path
from .views import RoomView

urlpatterns = [
    # .as_view(), take the class and give a view format
    path('', RoomView.as_view()),
]
