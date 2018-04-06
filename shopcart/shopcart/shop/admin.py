from django.contrib import admin
from .models import Manufacturer, Product

# Register your models here.
class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepoluated_fields = {'slug': ('name',)}
admin.site.register(Manufacturer, ManufacturerAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'manufacturer', 'point', 'stock', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated', 'manufacturer']
	list_editable = ['point', 'stock', 'available']
	prepoluated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
