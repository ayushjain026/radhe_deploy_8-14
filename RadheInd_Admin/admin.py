from django.contrib import admin
from RadheInd_Admin.models import productDetails, pageTitle, pageTitleOption


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


admin.site.register(pageTitle, adminPageTitle)
admin.site.register(pageTitleOption, adminPageTitleOption)
admin.site.register(productDetails, adminProductDetails)

