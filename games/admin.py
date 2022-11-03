from django.contrib import admin
from .models import *

# Register your models here.
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slogan', 'is_pub')
    list_display_links = ('title',)
    list_filter = ('title', 'slogan')
    search_fields = ('title', 'slogan')
    list_editable = ('is_pub',)
    prepopulated_fields = {'game_slug':('title',)}

admin.site.register(Games, GamesAdmin)

admin.site.register(Platforms)
admin.site.register(Category)
admin.site.register(Developers)
admin.site.register(GameScreen)
admin.site.register(SystemReq)