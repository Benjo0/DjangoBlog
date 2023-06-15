from django.urls import path
from . import views
from .views import AddPostView

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('add_post/', AddPostView.as_view() , name='add_post'),
]