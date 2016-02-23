from __future__ import unicode_literals
from django.db import models
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
    main_colour = models.CharField(max_length=30)
    author = models.ForeignKey(Author)

    pub_date = models.DateTimeField('date published')

    original_img = ImageField(upload_to=dir_name)
    #
    # admin_block_img = get_thumbnail(original_img, '150x150', crop='center', quality=50)
    #
    # block_img = get_thumbnail(original_img, '300x300', crop='center', quality=99)
    #
    # preview_img = get_thumbnail(original_img, '500x500', crop='center', quality=99)

    def image_thumb(self):
        im = get_thumbnail(self.original_img, '150x150', crop='center', quality=99)
        return u'<img src="%s" />' % im.url
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    def __unicode__(self):
        return self.title