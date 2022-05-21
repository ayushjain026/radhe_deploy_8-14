from django.urls import path

from RadheInd_Admin import views

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.test, name="test"),
    path('maintitle/', views.maintitle, name="maintitle"),
    path('title/', views.title, name="title"),
    path('details/', views.details, name="details"),
    path('addSubCategory/', views.addSubCategory, name="addSubCategory")

]
