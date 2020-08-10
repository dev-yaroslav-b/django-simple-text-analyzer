from django.urls import path
from .views import IndexView, create_post

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', create_post, name='create_post'),
]