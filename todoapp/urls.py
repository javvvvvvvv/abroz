from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

from todoapp import views

from todoapp.views import dialy

urlpatterns = [

    path('',views.dialy,name='dialy'),
    #  path('details/',views.details,name='details')
     path('delete<int:taskid>/',views.delete,name='delete'),
     path('update<int:id>/',views.update,name='update'),
     path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
     path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
     path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
     path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
]

