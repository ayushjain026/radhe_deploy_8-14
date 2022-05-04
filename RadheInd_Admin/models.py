from django.db import models


class pageTitle(models.Model):
    title = models.CharField(max_length=200)


class productDetails(models.Model):
    productTitle = models.CharField(max_length=500)
    productImage = models.FileField(upload_to='ProductImage', null=True)
    detail = models.CharField(max_length=5000)
    titleId = models.ForeignKey(pageTitle, on_delete=models.CASCADE, related_name="productdetails")


class testing(models.Model):
    txt = models.CharField(max_length=200)
