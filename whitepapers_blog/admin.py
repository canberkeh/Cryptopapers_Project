from django.contrib import admin
from . import models

# Register your models here.

class WhitePapersAdmin(admin.ModelAdmin):

    search_fields = ['name', 'symbol']
    list_filter = ['category']
    list_display = ['name', 'symbol', 'category']
    
    # If you turn active list_editable, you can edit category on Admin page
    # list_editable = ['category'] 

admin.site.register(models.WhitePapers, WhitePapersAdmin)

class UserProfileAdmin(admin.ModelAdmin):

    search_fields = ['username']
#     list_filter = ['username']

admin.site.register(models.UserProfileInfo)