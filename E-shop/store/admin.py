from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.profile import Profile


class AdminProduct(admin.ModelAdmin):
    list_display = ['brandname','category','weight','price']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email','password']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','brandname','variety','weight','quantity','price','address','phone','date','status']


class AdminProfile(admin.ModelAdmin):
    list_display = ['first_name','email']



#Register your models here.


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)
admin.site.register(Profile,AdminProfile)

