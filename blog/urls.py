from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('api/v1/masters/', views.MasterListCreateAPIview.as_view()),
    path('api/v1/masters/<int:id>/', views.MasterDetailUpdateDeleteAPIview.as_view()),
    path('api/v1/procedures/', views.ProcedureListCreateAPIview.as_view()),
    path('api/v1/procedures/<int:id>/', views.ProcedureDetailUpdateDeleteAPIview.as_view()),
    path('api/v1/branch/', views.BranchListCreateAPIview.as_view()),

]