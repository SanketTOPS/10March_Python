from django.contrib import admin
from .models import userdata


# Register your models here.
class userdataAdmin(admin.ModelAdmin):
    list_display=['id','name','sub','email','dob','mobile']


admin.site.register(userdata,userdataAdmin)
