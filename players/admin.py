from django.contrib import admin
from .models import Player, Club
# Register your models here.


@admin.register(Player)
class PlayerAdminSite(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'position', 'price']


admin.site.register(Club)