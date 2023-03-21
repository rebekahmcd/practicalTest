from django.contrib import admin
from django.urls import path
from django.urls import include
from weather import views

urlpatterns = [
    path('', views.page, name='page'),
    path('weather/', include('weather.urls')),
    path('admin/', admin.site.urls),
]
