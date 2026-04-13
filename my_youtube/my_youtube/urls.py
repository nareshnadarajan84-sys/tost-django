from django.contrib import admin
from django.urls import path
from video_hub import views # Import your views logic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # This makes the home page show your clone
]