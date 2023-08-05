from django.db import models


class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories_images/')

    def __str__(self):
        return self.name

    # @staticmethod
    # def get_all_categories():
    #     return category.objects.all()
    #
    # def __str__(self):
    #     return self.name


class Brand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class products(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return self.name

    # @staticmethod
    # def get_products_by_id(ids):
    #     return products.objects.filter(id__in=ids)
    #
    # @staticmethod
    # def get_all_products():
    #     return products.objects.all()
    #
    # @staticmethod
    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return products.objects.filter(category=category_id)
    #     else:
    #         return products.get_all_products();