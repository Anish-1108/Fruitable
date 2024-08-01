from django.db import models

# Create your models here.

class Contact_US(models.Model):
    
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

    
class user(models.Model):
    
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.TextField(max_length=10)
    otp=models.IntegerField(default=1234)

    def __str__(self):
        return self.email
  
    
class Categories(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    
    
class Add_product(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    categories_id = models.ForeignKey(Categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    qyt=models.IntegerField()
    des=models.TextField()
    pic=models.ImageField(upload_to="img")
    
    def __str__(self):
        return self.name
    
    
class Add_to_cart(models.Model):
    
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Add_product,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    qyt=models.IntegerField()
    pic=models.ImageField(upload_to="img")
    total_price = models.IntegerField()
    
    def __str__(self):
        return self.name


class Address(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField()
    list = models.TextField()    
    









    