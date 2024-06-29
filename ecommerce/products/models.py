from django.db import models

# Create your models here.
class Category(models.Model):
   category = models.CharField(max_length = 200)

   def __str__(self):
      return self.category

class AddProducts(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    unit = models.IntegerField()
    image = models.ImageField(upload_to='product/image',null=True)

    def __str__(self):
      return self.product_name