from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

class category(models.Model):
    
    category = models.CharField(max_length=100,null=False,unique=True)
    category_image = VersatileImageField(upload_to = 'category_image',ppoi_field='image_ppoi',blank =True)
    image_ppoi    = PPOIField()


    def __str__(self):
        return self.category



class brand(models.Model):

    brand_name = models.CharField(max_length=50)

    
    def __str__(self):
        return self.brand_name

class product_model(models.Model):

    category = models.ForeignKey(category,on_delete=models.CASCADE)
    brand = models.ForeignKey(brand,on_delete=models.CASCADE,)
    model_name = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name




class product(models.Model):

    date = models.DateField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    model = models.ForeignKey(product_model, on_delete=models.CASCADE)
    product_image = VersatileImageField(upload_to = 'product_image',ppoi_field='image_ppoi',blank =True)
    image_ppoi    = PPOIField()
    price = models.IntegerField()

    def __str__(self):
        return self.product_name


class cart(models.Model):
    date = models.DateField(auto_now_add=True)
    session_key = models.CharField(max_length=1000)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.name


