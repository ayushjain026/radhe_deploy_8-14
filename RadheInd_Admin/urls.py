from django.urls import path

from RadheInd_Admin import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.test, name="test"),
    path('title/', views.title, name="title"),
    path('details/', views.details, name="details")
]
