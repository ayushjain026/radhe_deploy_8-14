from django.contrib import admin
from RadheInd_Admin.models import productDetails, pageTitle


class adminPageTitle(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]


class adminProductDetails(admin.ModelAdmin):
    list_display = [
        'id',
        'detail',
        'titleId'
    ]



admin.site.register(pageTitle, adminPageTitle)
admin.site.register(productDetails, adminProductDetails)

