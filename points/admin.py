from django.contrib import admin
from .models import PlayerPoint
# Register your models here.


@admin.register(PlayerPoint)
class PlayerPointAdmin(admin.ModelAdmin):
    list_display = ['player', 'week', 'point']
    list_editable = ('point',)