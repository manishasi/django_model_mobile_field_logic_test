from django.contrib import admin
from .models import Moblie,Email
# Register your models here.
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display=('id','email')

@admin.register(Moblie)
class MobileAdmin(admin.ModelAdmin):
    list_display=('email_id','moblie')
