from django.contrib import admin

# Register your models here.
from . models import Category,Product
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepoluted_fields={'slug':('name',)}
admin.site.register(Category,CatagoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepoluted_fields={'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

