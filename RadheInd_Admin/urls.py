from django.urls import path
from RadheInd_Admin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('info/', views.test, name="test"),
    path('maintitle/', views.maintitle, name="maintitle"),
    path('title/', views.title, name="title"),
    path('details/', views.details, name="details"),
    path('addSubCategory/', views.addSubCategory, name="addSubCategory"),
    path('email_sending/', views.email_sending, name="email_sending")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
