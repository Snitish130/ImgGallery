
from django.urls import path
from app.views import gallery , viewPhoto , addPhoto  , filterByTag , rotateleftPhoto  , rotaterightPhoto , deletePhoto

urlpatterns = [
    path('', gallery , name='gallery'),
    path('viewphoto/<int:pk>', viewPhoto , name='viewPhoto'),
    path('rotateleftphoto/<int:pk>', rotateleftPhoto , name='rotateleftPhoto'),
    path('rotaterightphoto/<int:pk>', rotaterightPhoto , name='rotaterightPhoto'),
    path('deletephoto/<int:pk>', deletePhoto , name='deletePhoto'),
    path('tags/<str:slug>', filterByTag , name='filterByTag'),
    path('addphoto', addPhoto ),

]
