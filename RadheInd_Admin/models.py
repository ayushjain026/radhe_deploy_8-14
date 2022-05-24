from django.db import models


class pageTitle(models.Model):
    title = models.CharField(max_length=200)


class pageTitleOption(models.Model):
    title = models.CharField(max_length=200)
    productImage = models.ImageField(upload_to='ProductImage', null=True, blank='dafault.jpg')
    pageTitleId = models.ForeignKey(pageTitle, on_delete=models.CASCADE, related_name="productdetails")


class productDetails(models.Model):
    productTitle = models.CharField(max_length=500)
    detail = models.CharField(max_length=5000)
    titleId = models.ForeignKey(pageTitleOption, on_delete=models.CASCADE, related_name="productdetails")


class testing(models.Model):
    txt = models.CharField(max_length=200)
