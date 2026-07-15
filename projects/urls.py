from django.urls import path
from . import views

app_name='projects'
urlpatterns=[
    path('',views.ProjectsList.as_view(),name='ProjectList'), 
    path('add/',views.CreateProject.as_view(),name='add_project'),
    path('<int:pk>/',views.ProjectDetail.as_view(),name='project_detail'),
    path('update/<int:pk>/',views.UpdateProject.as_view(),name='update_project'),
    path('delete/<int:pk>/', views.DeleteProject.as_view(),name='delete_project'),



]