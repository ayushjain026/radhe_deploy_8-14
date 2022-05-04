from django.shortcuts import render

from RadheInd_Admin.models import *


def index(request):
    return render(request, "index.html")


def title(request):
    title = request.POST['title']
    data = pageTitle.objects.create(title=title)
    data.save()
    return render(request, 'test.html')


def details(request):
    if request.method == 'POST':
        detail = request.POST['P_detail']
        title = request.POST['P_title']
        image = request.FILES['P_image']
        id = request.POST['id']
        data1 = pageTitle.objects.get(id=id)
        data = productDetails.objects.create(detail=detail, titleId=data1, productTitle=title, productImage=image)
        data.save()
        return render(request, 'blog-details.html')
    else:
        id = request.GET['id']
        data1 = pageTitle.objects.get(id=id)
        # print(data1.title)
        data2 = productDetails.objects.filter(titleId=data1)
        for i in data2:
            print(i.titleId.title)
        title = "Design Of Fire Network"
        details = """The Fire protection system will basically consist of the Yard Hydrant system, Fire pump house, Fire Water Storage Tank, Fire Hose Reel System, and Automatic Sprinkler System.

We conduct Fire Gap Assessment and Designing of Entire Fire System (i.e. Hydrant Network and a sprinkler system) as per the TAC Guideline, Indian Standards, NFPA standards, NBC-2016, and Local CFO requirements."""
        return render(request, 'radhedetails.html', {"content":data2, "pagetitle":data1.title})


def test(request):
    data = testing.objects.all()
    print(data)
    a = "Hello this is data"
    return render(request, "test.html", {"a":a, 'data':data})

