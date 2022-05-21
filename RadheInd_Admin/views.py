import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from RadheInd_Admin.models import *
from main_app import settings


def index(request):
    main_title = pageTitle.objects.all()
    titleSubOption = pageTitleOption.objects.all()
    return render(request, "index.html", {'main_title':main_title, 'titleSubOption':titleSubOption})


def maintitle(request):
    title = request.POST['title']
    data = pageTitle.objects.create(title=title)
    data.save()
    return render(request, 'test.html')


def title(request):
    title = request.POST['title']
    maintitleObj = pageTitle.objects.get(id=request.POST['id'])
    data = pageTitleOption.objects.create(title=title, pageTitleId=maintitleObj)
    data.save()
    return render(request, 'test.html')


def details(request):
    if request.method == 'POST':
        detail = request.POST['P_detail']
        title = request.POST['P_title']
        image = request.FILES['P_image']
        id = request.POST['id']
        data1 = pageTitleOption.objects.get(id=id)
        data1.productImage = image
        data = productDetails.objects.create(detail=detail, titleId=data1, productTitle=title)
        data.save()
        data1.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        id = request.GET['id']
        data1 = pageTitleOption.objects.get(id=id)
        base_dir = settings.MEDIA_ROOT
        image = os.path.join(base_dir, str(data1.productImage.url))
        data2 = productDetails.objects.filter(titleId=data1)
        # for i in data2:
        #     print(i.titleId.title)
        main_title = pageTitle.objects.all()
        titleSubOption = pageTitleOption.objects.all()
        return render(request, 'radhedetails.html', {"content":data2, 'image':image, 'data1':data1, "pagetitle":data1.title, 'main_title':main_title, 'titleSubOption':titleSubOption})


def addSubCategory(request):
    if request.method == "POST":
        title = request.POST['title']
        maintitleObj = pageTitle.objects.get(id=request.POST['id'])
        data = pageTitleOption.objects.create(title=title, pageTitleId=maintitleObj)
        data.save()
        return redirect('/')
    else:
        title = pageTitle.objects.get(id=request.GET['id'])
        return render(request, "SubCategory.html", {'title':title})


def test(request):
    data = testing.objects.all()
    print(data)
    a = "Hello this is data"
    return render(request, "test.html", {"a":a, 'data':data})

