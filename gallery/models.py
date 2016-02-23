from __future__ import unicode_literals
from django.db import models
from PIL import Image
from sorl.thumbnail import ImageField, get_thumbnail

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


class Exhibit(models.Model):
    title = models.CharField(max_length=30)
    creation_date = models.DateField()
    country = models.CharField(max_length=30)
    style = models.CharField(max_length=30)

    #COLORS
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

    main_colour = models.CharField(max_length=7,
                                   choices=MAIN_COLOR_CHOICES,
                                   default=WHITE)

    author = models.ForeignKey(Author)

    pub_date = models.DateTimeField('date published')

    original_img = ImageField(upload_to=dir_name)

    def image_thumb(self):
        im = get_thumbnail(self.original_img, '150x150', crop='center', quality=99)
        return u'<img src="%s" />' % im.url
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    def __unicode__(self):
        return self.title