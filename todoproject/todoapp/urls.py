from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('homep/',views.Tasklistview.as_view(),name='homep'),
    path('cgvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cgvdetail'),
    path('cgvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cgvupdate'),
    path('cgvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cgvdelete'),
]
