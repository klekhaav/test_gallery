from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
import datetime

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, blank=True, null=True)
    with_us = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


def dir_name(self, filename):
    url = "%s/%s" % (self.author.last_name, filename)
    return url


class Color(models.Model):
    BLACK = '#000000'
    GRAY = '#808080'
    SILVER = '#C0C0C0'
    WHITE = '#FFFFFF'
    MAROON = '#800000'
    RED = '#FF0000'
    OLIVE = '#808000'
    YELLOW = '#FFFF00'
    GREEN = '#008000'
    LIME = '#00FF00'
    TEAL = '#008080'
    AQUA = '#00FFFF'
    NAVY = '#000080'
    BLUE = '#0000FF'
    PURPLE = '#800080'
    FUNCHSIA = '#FF00FF'

    MAIN_COLOR_CHOICES = (
        (BLACK, 'black'), (GRAY, 'gray'), (SILVER, 'silver'),
        (WHITE, 'white'), (MAROON, 'maroon'), (RED, 'red'),
        (OLIVE, 'olive'), (YELLOW, 'yellow'), (GREEN, 'green'),
        (LIME, 'lime'), (TEAL, 'teal'), (AQUA, 'aqua'), (NAVY, 'navy'),
        (BLUE, 'blue'), (PURPLE, 'purple'), (FUNCHSIA, 'funchsia'),
    )

    main_color = models.CharField(max_length=8,
                                  choices=MAIN_COLOR_CHOICES,
                                  default=WHITE)

    def __unicode__(self):
        return u'%s' % self.main_color


class Exhibit(models.Model):
    title = models.CharField(max_length=30)
    creation_date = models.DateField()
    country = models.CharField(max_length=30)
    author = models.ForeignKey(Author)
    pub_date = models.DateField('date published')
    original_img = ImageField(upload_to=dir_name)

    def image_thumb(self):
        im = get_thumbnail(self.original_img, '150x150', crop='center', quality=99)
        return u'<img src="%s" />' % im.url
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    def was_published_recently(self):
        return self.pub_date <= datetime.date.today()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published?'

    class Meta:
        abstract = True


class PaintStyle(models.Model):
    style = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.style


class PaintSubject(models.Model):
    subject = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.subject


class PaintMedium(models.Model):
    medium = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.medium


class Paint(Exhibit):
    style = models.ForeignKey(PaintStyle)
    subject = models.ForeignKey(PaintSubject)
    medium = models.ForeignKey(PaintMedium)
    main_color = models.ForeignKey(Color)


class PhotoStyle(models.Model):
    style = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.style


class PhotoSubject(models.Model):
    subject = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.subject


class PhotoMedium(models.Model):
    medium = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.medium


class Photo(Exhibit):
    style = models.ForeignKey(PhotoStyle)
    subject = models.ForeignKey(PhotoSubject)
    medium = models.ForeignKey(PhotoMedium)


class DrawStyle(models.Model):
    style = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.style


class DrawSubject(models.Model):
    subject = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.subject


class DrawMedium(models.Model):
    medium = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.medium


class Draw(Exhibit):
    style = models.ForeignKey(DrawStyle)
    subject = models.ForeignKey(DrawSubject)
    medium = models.ForeignKey(DrawMedium)
    main_color = models.ForeignKey(Color)


class SculptStyle(models.Model):
    style = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.style


class SculptSubject(models.Model):
    subject = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.subject


class SculptMedium(models.Model):
    medium = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.medium


class Sculpt(Exhibit):
    style = models.ForeignKey(SculptStyle)
    subject = models.ForeignKey(SculptSubject)
    medium = models.ForeignKey(SculptMedium)


class CollageStyle(models.Model):
    style = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.style


class CollageSubject(models.Model):
    subject = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.subject


class CollageMedium(models.Model):
    medium = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.medium


class Collage(Exhibit):
    style = models.ForeignKey(CollageStyle)
    subject = models.ForeignKey(CollageSubject)
    medium = models.ForeignKey(CollageMedium)


class PrintStyle(models.Model):
    style = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.style


class PrintSubject(models.Model):
    subject = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.subject


class PrintMedium(models.Model):
    medium = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s' % self.medium


class Print(Exhibit):
    style = models.ForeignKey(PrintStyle)
    subject = models.ForeignKey(PrintSubject)
    medium = models.ForeignKey(PrintMedium)
    main_color = models.ForeignKey(Color)
