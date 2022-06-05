import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from RadheInd_Admin.models import *
from main_app import settings
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    main_title = pageTitle.objects.all()
    titleSubOption = pageTitleOption.objects.all()
    our_services = pageTitle.objects.all()[:3]
    support_data = support.objects.get(id=1)
    return render(request, "index-2.0.html", {'main_title':main_title, 'titleSubOption':titleSubOption, 'our_services':our_services, 'support_data':support_data})


def maintitle(request):
    main_title = pageTitle.objects.all()
    titleSubOption = pageTitleOption.objects.all()
    title = request.POST['title']
    data = pageTitle.objects.create(title=title)
    data.save()
    messages.success(request, f"New Service {title} added sucessfully")
    return render(request, 'main_title.html', {'main_title':main_title, 'titleSubOption':titleSubOption})


def delete_title(request):
    title_id = request.GET['id']
    data = pageTitle.objects.get(id=title_id)
    data.delete()
    messages.success(request, f"Title = {data.title} Deleted Sucessfull")
    return redirect(request.META['HTTP_REFERER'])


def title(request):
    title = request.POST['title']
    maintitleObj = pageTitle.objects.get(id=request.POST['id'])
    data = pageTitleOption.objects.create(title=title, pageTitleId=maintitleObj)
    data.save()
    messages.success(request, f"New Service {title} added sucessfully")
    return render(request, 'main_title.html')


def details(request):
    if request.method == 'POST':
        detail = request.POST['P_detail']
        title = request.POST['P_title']
        # image = request.FILES['P_image']
        id = request.POST['id']
        data1 = pageTitleOption.objects.get(id=id)
        # data1.productImage = image
        data = productDetails.objects.create(detail=detail, titleId=data1, productTitle=title)
        data.save()
        data1.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        id = request.GET['id']
        data1 = pageTitleOption.objects.get(id=id)
        print(data1.productImage)
        data2 = productDetails.objects.filter(titleId=data1)
        main_title = pageTitle.objects.all()
        titleSubOption = pageTitleOption.objects.all()
        return render(request, 'radhedetails.html', {"content":data2, 'data1':data1, "pagetitle":data1.title, 'main_title':main_title, 'titleSubOption':titleSubOption})


def addSubCategory(request):
    if request.method == "POST":
        title = request.POST['title']
        P_image = request.FILES['P_image']
        maintitleObj = pageTitle.objects.get(id=request.POST['id'])
        data = pageTitleOption.objects.create(title=title, productImage=P_image, pageTitleId=maintitleObj)
        data.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        main_title = pageTitle.objects.all()
        titleSubOption = pageTitleOption.objects.all()
        title = pageTitle.objects.get(id=request.GET['id'])
        return render(request, "SubCategory.html", {'title':title, 'main_title':main_title, 'titleSubOption':titleSubOption})

def email_sending(request):
    name = request.GET['name']
    email = request.GET['email']
    sub = request.GET['subject']
    message = request.GET['message']
    print(f"name = {name}\nemail = {email}\nsub = {sub}\nmessage = {message}")

    subject = f"Customer"
    message = (f"name = {name}\nemail = {email}\nsub = {sub}\nmessage = {message}")
    from_email = settings.EMAIL_HOST
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    messages.success(request, f"Thank you!\nWe will contact you ASAP")
    return redirect(request.META['HTTP_REFERER'])


def delete_servce_content(request):
    id = request.GET['id']
    data = productDetails.objects.get(id=id)
    data.delete()
    return redirect(request.META['HTTP_REFERER'])


def edit_servce_content(request):
    id = request.GET["id"]
    details = request.GET["details"]
    data = productDetails.objects.get(id=id)
    data.detail = details
    data.save()
    return redirect(request.META['HTTP_REFERER'])


def testimonialPage(request):
    if request.method == 'POST':
        data = testimonials.objects.create(
            company_logo = request.FILES['companyLogo'],
            Company_name = request.POST['companyName'],
            customer_name = request.POST['customerName'],
            customer_position = request.POST['customerPosition'],
            feedback = request.POST['customerFeedback']
        )
        data.save()
        messages.success(request, f"Testimonial of company {request.POST['companyName']} Added Sucessfully")
        return redirect(request.META['HTTP_REFERER'])
    else:
        data = testimonials.objects.all()
        main_title = pageTitle.objects.all()
        titleSubOption = pageTitleOption.objects.all()
        return render(request, "testimonials.html", {'data':data, 'main_title':main_title, 'titleSubOption':titleSubOption})


def companyCertificates(request):
    if request.method == 'POST':
        data = certificates.objects.create(
            certificateImage = request.FILES['certificateImage'],
            certificateName = request.POST['certificateName'],
        )
        data.save()
        messages.success(request, f"Certificate Added Sucessfully")
        return redirect(request.META['HTTP_REFERER'])
    else:
        data = certificates.objects.all()
        main_title = pageTitle.objects.all()
        titleSubOption = pageTitleOption.objects.all()
        return render(request, "certificate.html", {'data':data, 'main_title':main_title, 'titleSubOption':titleSubOption})


def aboutus(request):
    main_title = pageTitle.objects.all()
    titleSubOption = pageTitleOption.objects.all()
    return render(request, "aboutus.html", {'main_title':main_title, 'titleSubOption':titleSubOption})


def test(request):
    data = testing.objects.all()
    main_title = pageTitle.objects.all()
    return render(request, "main_title.html", {'data':data, 'main_title':main_title})

