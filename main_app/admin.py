from django.contrib import admin
from .models import book, category
# Register your models here.
admin.site.register(category)
admin.site.register(book)
