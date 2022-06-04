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


admin.site.register(pageTitle, adminPageTitle)
admin.site.register(pageTitleOption, adminPageTitleOption)
admin.site.register(productDetails, adminProductDetails)
admin.site.register(support, adminSupport)
admin.site.register(testimonials)



