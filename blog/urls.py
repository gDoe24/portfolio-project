
from django.urls import path
from django.conf.urls import url

from . import views



urlpatterns = [
    path('', views.allblogs, name="allblogs" ),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('<int:pk>/add_comment/',views.add_comment, name='add_comment'),
]