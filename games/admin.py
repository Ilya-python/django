from django.contrib import admin
from .models import *


# Register your models here.
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slogan', 'is_pub')
    list_display_links = ('title',)
    list_filter = ('title', 'slogan')
    search_fields = ('title', 'slogan')
    list_editable = ('is_pub',)
    prepopulated_fields = {'game_slug': ('title',)}


class DevelopersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'dev_slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('title',)}


admin.site.register(Games, GamesAdmin)
admin.site.register(RaitingStar)
admin.site.register(Raiting)
admin.site.register(Platforms)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Developers, DevelopersAdmin)
admin.site.register(GameScreen)
admin.site.register(SystemReq)
