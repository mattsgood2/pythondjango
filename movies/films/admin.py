from django.contrib import admin

from .models import Film, FilmListDetail

# Register your models here.

class FilmListDetailInline(admin.StackedInline):
    model = FilmListDetail


class FilmAdmin(admin.ModelAdmin):
    inlines = [
        FilmListDetailInline,
        ]


admin.site.register(Film, FilmAdmin)
admin.site.register(FilmListDetail)
