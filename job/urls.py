from django.urls import path,include
from . import views 
from . import api

app_name = 'job'

urlpatterns = [
    path('',views.job_list, name='job_list'),
    path('post',views.post_job, name='post_job'),
    path('<str:slug>',views.job_detail,name='job_detail'),
    path('api/list',api.job_list_api,name='job_list_api'),
    path('api/detail/<int:id>',api.job_detail_api,name='job_detail_api'),
]