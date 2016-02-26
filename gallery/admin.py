from django.contrib import admin

# Register your models here.

from models import *


class ExhibitAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Exhibit',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',     {'fields':  ['creation_date', 'country']}),
        ('Specification',   {'fields':  ['ex_type', 'main_colour']}),
        ('Publication date', {'fields': ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'pub_date', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'creation_date', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['last_name', 'first_name']}),
        ('Contacts',        {'fields': ['email'], 'classes': ['collapse']}),
        ('With us from',    {'fields': ['with_us']}),
    ]
    list_display = ('last_name', 'first_name', 'email', 'with_us')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('with_us',)


admin.site.register(Author, AuthorsAdmin)
admin.site.register(Exhibit, ExhibitAdmin)

