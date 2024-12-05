from django.contrib import admin
from .models import Document,assembly

# Register your models here.
class shora(admin.ModelAdmin):

    list_display = ('user', 'receipt_image')

admin.site.register(Document, shora )

class Assembly(admin.ModelAdmin):

    list_display = ('user', 'receipt_image')

admin.site.register(assembly, Assembly )