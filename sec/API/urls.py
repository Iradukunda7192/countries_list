from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from .views import home_page
urlpatterns = [
  
    path('', views.index, name='request '),
    
    path('home/', home_page, name='home'),
]


