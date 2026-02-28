from django.db import models

genderChoice = (
    ("Male" , "Male"),
    ("Female" , "Female")
)

discountChoice = (
    ("%","%"),
    ("Rs","Rs")
)

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.BigIntegerField(max_length=10)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=genderChoice,default="Male")
    #gender = models.Choices(genderChoice)

    def __str__(self):
        return self.email
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category/",default="")

    def __str__(self):
        return self.name
    
class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="subCategory/",default="")

    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="product/",default="")
    price = models.BigIntegerField(max_length=10)
    discountType = models.CharField(max_length=6,choices=discountChoice,default="%")
    discount = models.BigIntegerField(max_length=10)

    def __str__(self):
        return self.name