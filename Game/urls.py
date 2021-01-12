from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('catagory/<int:cid>', views.catagory, name='catagory'),
    
]
