from django.db import models

# Create your models here.

def content_file_name(instance, filename):
    return '/'.join(['product', str(instance.name), filename])

class Product(models.Model):
    barcode=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to=content_file_name,default="/product/700x300.png")

    def __str__(self):
        return self.name


class Review(models.Model):
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        title=models.CharField(max_length=100)
        text=models.CharField(max_length=500)

        def __str__(self):
            return self.title

