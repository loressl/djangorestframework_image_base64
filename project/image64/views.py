from django.shortcuts import render
from .models import *
from .serializers import *
from .utils import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@csrf_exempt
def get_images(request):
    images= Image_Base64.objects.all()
    if not images:
        return HttpResponse("There are no images in the database.", status=status.HTTP_404_NOT_FOUND)
    serializer = Image_Base64Serializer(images, many=True)
    return JsonResponse(serializer.data, status= status.HTTP_200_OK, safe=False)

@api_view(['GET'])
@csrf_exempt
def get_image_id(request, id):
    try:
        image= Image_Base64.objects.get(id=id)
    except Image_Base64.DoesNotExist:
        return HttpResponse("There are no image in the database.", status=status.HTTP_404_NOT_FOUND)
    image_base64 = get_image_base64(image.image,80)
    serializer= Image_Base64Serializer(image)
    return JsonResponse(serializer.data, status= status.HTTP_200_OK, safe=False)
    
@api_view(['POST'])
@csrf_exempt
def save_base64(request):
    data= JSONParser().parse(request)
    image_base64 = get_image_base64(data['image'],80)
    serializer = Image_Base64Serializer(data={'image':str(image_base64)})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status= status.HTTP_201_CREATED, safe=False)  
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST) 
    