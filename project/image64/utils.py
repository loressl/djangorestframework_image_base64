import base64, secrets,io
from PIL import Image
from django.core.files.base import ContentFile

#ref: https://dev.to/ageumatheus/creating-image-from-dataurl-base64-with-pyhton-django-454g

def get_image_base64(data_url, scale_percent):
    #getting the file format and the necessary dataURL for the file
    _format, _dataurl = data_url.split(';base64,')
    
    #file name and extension
    _filename, _extension = secrets.token_hex(20), _format.split('/')[-1]
    
    #generating the contents of the file
    file = ContentFile(base64.b64decode(_dataurl), name=f"{_filename}.{_extension}")
    
    #opening the file with the pillow
    image = Image.open(file)
    #image.show()

    #using BytesIO to rewrite the new content without using the filesystem
    image_io= io.BytesIO()
    
    #resize
    width =int(image.size[0]*scale_percent/100)
    height= int(image.size[1]*scale_percent/100)
    image = image.resize((width,height),Image.ANTIALIAS)
    
    #save resized image
    image.save(image_io, format=_extension)
    
    second_part= str(base64.b64encode(image_io.getvalue())).split("'")[1]
    image_base64= "data:image/jpeg;base64,"+ second_part
   
    return image_base64
    
    