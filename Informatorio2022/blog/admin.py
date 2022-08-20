from django.contrib import admin
from django.template.defaultfilters import slugify
from .models import Post

# Register your models here.
class postAdmin(admin.ModelAdmin):
    #list_display = ("title", "body",)
    prepopulated_fields = {"slug": ("titulo",)}
    
admin.site.register(Post, postAdmin)