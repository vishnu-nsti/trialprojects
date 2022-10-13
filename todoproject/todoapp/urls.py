from.import views
from django.urls import path

urlpatterns = [
    path('',views.task,name='task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.listview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.detailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete')
]