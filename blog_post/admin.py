from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(Catagory)
class catagoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)