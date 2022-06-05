from django.contrib import admin
from RadheInd_Admin.models import *


class adminPageTitle(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


class adminPageTitleOption(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'productImage',
        'pageTitleId'
    ]


class adminProductDetails(admin.ModelAdmin):
    list_display = [
        'id',
        'detail',
        'titleId',
        'productTitle'
    ]


class adminSupport(admin.ModelAdmin):
    list_display = [
        'happyClients',
        'projects',
        'hoursOfSupport',
        'hardWork'
    ]


class adminTestimonial(admin.ModelAdmin):
    list_display = [
        'Company_name',
        'company_logo',
        'customer_name',
        'customer_position',
        'feedback',
    ]
    search_fields = ['Company_name', 'customer_name', 'customer_position', 'feedback']

class adminCertificates(admin.ModelAdmin):
    list_display = [
        'certificateName',
        'certificateImage',
    ]
    search_fields = ['certificateName']


admin.site.register(pageTitle, adminPageTitle)
admin.site.register(pageTitleOption, adminPageTitleOption)
admin.site.register(productDetails, adminProductDetails)
admin.site.register(support, adminSupport)
admin.site.register(testimonials, adminTestimonial)
admin.site.register(certificates, adminCertificates)












