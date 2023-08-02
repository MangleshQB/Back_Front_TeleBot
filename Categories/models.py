from django.db import models


class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class products(models.Model):
    category_name = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return self.name
