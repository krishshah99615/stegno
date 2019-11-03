from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Image
from PIL import Image as im
from .forms import *
from .stegno import  encode as e
from .stegno import  decode as d
from wsgiref.util import FileWrapper
import mimetypes
# Create your views here.
def home(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            i = Image.objects.latest('id')

            return render(request, 'home.html', {'form' : form,'isup':'1','imgurl':i.img.url})

    else:
        form = UploadForm()
        return render(request, 'home.html', {'form' : form})

def encode(request):
    if request.POST:
        imageobj = Image.objects.latest('id')
        imageobj.img.open()
        image = im.open(imageobj.img)
        inputtext = request.POST['inputtext']
        e(image,inputtext)









        return render(request, 'home.html', {'isup':'1','imgurl':imageobj.img.url})
    else:
        return HttpResponse("Error")
def decode(request):
    if request.POST:
        imageobj = Image.objects.latest('id')
        imageobj.img.open()
        image = im.open(imageobj.img)

        decoded= d(image)
        return render(request, 'home.html', {'isup':'1','imgurl':imageobj.img.url,'text':str(decoded)})
    else:
        return HttpResponse("Error")
