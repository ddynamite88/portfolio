from django.urls import path
from . import views
import jobs.views
import blog.views
urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('home', jobs.views.home, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
