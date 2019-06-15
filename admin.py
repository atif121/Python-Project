from django.contrib import admin
# Register your models here.
from .models import Category, Book

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','image','created_at','updated_at']
    list_filter = ['available','created_at','updated_at']
    list_editable = ['price','stock','available','image']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Book,BookAdmin)