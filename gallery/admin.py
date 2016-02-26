from django.contrib import admin

# Register your models here.

from models import *


class PaintStyleAdmin(admin.ModelAdmin):
    fields = ['style']
    list_display = ('style',)
    search_fields = ('style',)
    list_filter = ['style']


class PaintSubjectAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ('subject',)
    search_fields = ('subject',)
    list_filter = ['subject']


class PaintMediumAdmin(admin.ModelAdmin):
    fields = ['medium']
    list_display = ('medium',)
    search_fields = ('medium',)
    list_filter = ['medium']


class PaintAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Painting',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',      {'fields':  ['creation_date', 'country']}),
        ('Specification',    {'fields':  ['style', 'subject', 'medium']}),
        ('Publication date', {'fields':  ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'style', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'style', 'creation_date', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class PhotoStyleAdmin(admin.ModelAdmin):
    fields = ['style']
    list_display = ('style',)
    search_fields = ('style',)
    list_filter = ['style']


class PhotoSubjectAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ('subject',)
    search_fields = ('subject',)
    list_filter = ['subject']


class PhotoMediumAdmin(admin.ModelAdmin):
    fields = ['medium']
    list_display = ('medium',)
    search_fields = ('medium',)
    list_filter = ['medium']


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Painting',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',      {'fields':  ['creation_date', 'country']}),
        ('Specification',    {'fields':  ['style', 'subject', 'medium']}),
        ('Publication date', {'fields':  ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'style', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'style', 'creation_date', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class DrawStyleAdmin(admin.ModelAdmin):
    fields = ['style']
    list_display = ('style',)
    search_fields = ('style',)
    list_filter = ['style']


class DrawSubjectAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ('subject',)
    search_fields = ('subject',)
    list_filter = ['subject']


class DrawMediumAdmin(admin.ModelAdmin):
    fields = ['medium']
    list_display = ('medium',)
    search_fields = ('medium',)
    list_filter = ['medium']


class DrawAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Painting',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',      {'fields':  ['creation_date', 'country']}),
        ('Specification',    {'fields':  ['style', 'subject', 'medium']}),
        ('Publication date', {'fields':  ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'style', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'style', 'creation_date', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class SculptStyleAdmin(admin.ModelAdmin):
    fields = ['style']
    list_display = ('style',)
    search_fields = ('style',)
    list_filter = ['style']


class SculptSubjectAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ('subject',)
    search_fields = ('subject',)
    list_filter = ['subject']


class SculptMediumAdmin(admin.ModelAdmin):
    fields = ['medium']
    list_display = ('medium',)
    search_fields = ('medium',)
    list_filter = ['medium']


class SculptAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Painting',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',      {'fields':  ['creation_date', 'country']}),
        ('Specification',    {'fields':  ['style', 'subject', 'medium']}),
        ('Publication date', {'fields':  ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'style', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'style', 'creation_date', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class CollageStyleAdmin(admin.ModelAdmin):
    fields = ['style']
    list_display = ('style',)
    search_fields = ('style',)
    list_filter = ['style']


class CollageSubjectAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ('subject',)
    search_fields = ('subject',)
    list_filter = ['subject']


class CollageMediumAdmin(admin.ModelAdmin):
    fields = ['medium']
    list_display = ('medium',)
    search_fields = ('medium',)
    list_filter = ['medium']


class CollageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Painting',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',      {'fields':  ['creation_date', 'country']}),
        ('Specification',    {'fields':  ['style', 'subject', 'medium']}),
        ('Publication date', {'fields':  ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'style', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'style', 'creation_date', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class PrintStyleAdmin(admin.ModelAdmin):
    fields = ['style']
    list_display = ('style',)
    search_fields = ('style',)
    list_filter = ['style']


class PrintSubjectAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ('subject',)
    search_fields = ('subject',)
    list_filter = ['subject']


class PrintMediumAdmin(admin.ModelAdmin):
    fields = ['medium']
    list_display = ('medium',)
    search_fields = ('medium',)
    list_filter = ['medium']


class PrintAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Painting',         {'fields':  ['title', 'author', 'original_img', 'image_thumb']}),
        ('Description',      {'fields':  ['creation_date', 'country']}),
        ('Specification',    {'fields':  ['style', 'subject', 'medium']}),
        ('Publication date', {'fields':  ['pub_date']}),
    ]
    readonly_fields = ['image_thumb']
    list_display = ('title', 'author', 'style', 'creation_date', 'image_thumb', 'was_published_recently')
    search_fields = ('title', 'author', 'style', 'creation_date', 'pub_date', 'was_published_recently')
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
admin.site.register(Paint, PaintAdmin)
admin.site.register(PaintStyle, PaintStyleAdmin)
admin.site.register(PaintSubject, PaintSubjectAdmin)
admin.site.register(PaintMedium, PaintMediumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoStyle, PhotoStyleAdmin)
admin.site.register(PhotoSubject, PhotoSubjectAdmin)
admin.site.register(PhotoMedium, PhotoMediumAdmin)
admin.site.register(Draw, DrawAdmin)
admin.site.register(DrawStyle, DrawStyleAdmin)
admin.site.register(DrawSubject, DrawSubjectAdmin)
admin.site.register(DrawMedium, DrawMediumAdmin)
admin.site.register(Sculpt, SculptAdmin)
admin.site.register(SculptStyle, SculptStyleAdmin)
admin.site.register(SculptSubject, SculptSubjectAdmin)
admin.site.register(SculptMedium, SculptMediumAdmin)
admin.site.register(Collage, CollageAdmin)
admin.site.register(CollageStyle, CollageStyleAdmin)
admin.site.register(CollageSubject, CollageSubjectAdmin)
admin.site.register(CollageMedium, CollageMediumAdmin)
admin.site.register(Print, PrintAdmin)
admin.site.register(PrintStyle, PrintStyleAdmin)
admin.site.register(PrintSubject, PrintSubjectAdmin)
admin.site.register(PrintMedium, PrintMediumAdmin)

