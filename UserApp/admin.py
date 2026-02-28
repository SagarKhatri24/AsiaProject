from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["name","email","contact","password","gender"]

admin.site.register(UserModel,UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","image"]
admin.site.register(CategoryModel,CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id","category","name","image"]
admin.site.register(SubCategoryModel,SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","category","subCategory","name","image","price","discountType","discount"]
admin.site.register(ProductModel,ProductAdmin)