from django.contrib import admin
from .import models
# Register your models here.
class productAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'product_name', 'category','brand','model','price','product_image')
    search_fields = ['id','product_name']
    #list_display = ['your fields',]

 
  
    

  
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','category','category_image')
    search_fields = ['id','category']
    prepopulated_fields = {'slug':('category',)}
    
   
  


class modelsAdmin(admin.ModelAdmin):
    list_display = ('id','brand','model_name')
    search_fields = ['id','brand']
    prepopulated_fields = {'slug':('model_name',)}
 
class brandAdmin(admin.ModelAdmin):
    list_display = ('id','brand_name')
    search_fields = ['id','category']
    prepopulated_fields = {'slug':('brand_name',)}

class cartAdmin(admin.ModelAdmin):
    list_display = ('id','session_key','product')
  
class Contacts(admin.ModelAdmin):
    list_display = ('name','phone','email','subject','message')
  
admin.site.register(models.category,categoryAdmin)
admin.site.register(models.brand,brandAdmin)
admin.site.register(models.product_model,modelsAdmin)
admin.site.register(models.product,productAdmin)
admin.site.register(models.cart,cartAdmin)
admin.site.register(models.Contact,Contacts)

