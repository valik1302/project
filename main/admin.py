from django.contrib import admin
from .models import Blog_news, Categories
from tinymce.widgets import TinyMCE
from django.db import models
class Blog_newsAdmin(admin.ModelAdmin):
	"""fields ['date', 'tittle', 'text', 'published_date']"""
	formfield_overrides = {models.TextField : {'widget' : TinyMCE()}}
	"""fieldsets=[("Tittle and Date", {"fields": ['date', 'tittle']}), ("Content", {"fields":['text', 'published_date']})]"""
# Register your models here.
admin.site.register(Blog_news, Blog_newsAdmin)
admin.site.register(Categories)