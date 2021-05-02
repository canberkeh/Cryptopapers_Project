from django.contrib import admin
from . import models

# Register your models here.

class CoinRankingAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'like', 'dislike', 'hodl', 'total_points']
    
admin.site.register(models.CoinRanking, CoinRankingAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['coin_name', 'comment', 'like', 'dislike', 'create_date']

admin.site.register(models.Comments, CommentsAdmin)