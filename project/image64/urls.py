from django.urls import path
from .views import *

urlpatterns = [
    path('base64/<int:id>', get_image_id),
    path('base64/', get_images),
    path('save_base64/', save_base64),
]
