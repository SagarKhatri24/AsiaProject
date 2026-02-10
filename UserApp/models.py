from django.db import models

genderChoice = (
    ("Male" , "Male"),
    ("Female" , "Female")
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