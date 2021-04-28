from django.contrib import admin
from . import models

# Register your models here.

class CoinRankingAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'like', 'dislike', 'hodl', 'total_points']
admin.site.register(models.CoinRanking, CoinRankingAdmin)
