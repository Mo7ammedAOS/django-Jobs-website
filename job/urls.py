from django.urls import path,include
from . import views

app_name = 'job'

urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('post',views.post_job, name='post_job'),
    path('<str:slug>',views.job_detail,name='job_detail'),
]