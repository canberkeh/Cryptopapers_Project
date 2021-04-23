from django.contrib import admin
from . import models

# Register your models here.

class CoinRankingAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(models.CoinRanking, CoinRankingAdmin)
