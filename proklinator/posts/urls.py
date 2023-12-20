from django.urls import path
from . import api

urlpatterns = [
    path('like', api.LikeAPI.as_view()),
    path('', api.PostsAPI.as_view()),
]