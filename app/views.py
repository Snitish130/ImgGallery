
from django.shortcuts import render , redirect
from app.forms import PhotoForm
from app.models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PIL import Image as PilImage


def gallery(request):
    photos_list = Photo.objects.all()
    alltags = Photo.tags.all().distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(photos_list, 8)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    context = { 
            'photos' : photos,
            'alltags': alltags
        }  
    return render(request , 'gallery.html' , context = context)

def filterByTag(request , slug):
    photos = Photo.objects.filter(tags__name__in=[slug])
    context = { 
            'photos' : photos
        }  
    return render(request , 'gallery.html' , context = context)

def viewPhoto(request , pk):
    photo = Photo.objects.get(pk=pk)
    context = { 
            'photo' : photo
        }
    return render(request , 'photos.html' , context=context )

def rotateleftPhoto(request , pk):
    photo = Photo.objects.get(pk=pk)
    im = PilImage.open(photo.image)
    newphoto = im.rotate(90, expand=True)
    newphoto.save(photo.image.file.name, overwrite=True)
    context = { 
            'photo' : photo
        }
    return render(request , 'photos.html' , context=context )

def rotaterightPhoto(request , pk):
    photo = Photo.objects.get(pk=pk)
    im = PilImage.open(photo.image)
    newphoto = im.rotate(-90, expand=True)
    newphoto.save(photo.image.file.name, overwrite=True)
    context = { 
            'photo' : photo
        }
    return render(request , 'photos.html' , context=context )

def deletePhoto(request , pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
     
    return redirect('gallery')

def addPhoto(request):
    if request.method=='GET':
        form = PhotoForm()
        context = { 
            'form' : form
        }
        return render(request , 'addPhoto.html' , context=context)
    else:
        form = PhotoForm(request.POST , request.FILES)
        if form.is_valid:
            form.save()
            return redirect('gallery')
            
