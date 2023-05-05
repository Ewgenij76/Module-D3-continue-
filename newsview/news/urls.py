from django.urls import path
from .views import *


urlpatterns = [
    path('postlist', PostList.as_view()),
    path('postdetail/<int:pk>/', PostDetail.as_view()),

]
