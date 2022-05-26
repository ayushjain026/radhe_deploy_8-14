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


class testimonials(models.Model):
    company_logo = models.ImageField(upload_to='CompanyLogo', null=True, blank='dafault.jpg')
    Company_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_position = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500)


class certificates(models.Model):
    certificateImage = models.ImageField(upload_to="CompanyCertificates", null=True, blank='dafault.jpg')
    certificateName = models.CharField(max_length=100)


class testing(models.Model):
    txt = models.CharField(max_length=200)
