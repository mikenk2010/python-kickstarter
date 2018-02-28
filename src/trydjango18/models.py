from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_add')
    last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_edit')
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):  # Python 3.3 is __str__
        return self.title


def pre_save_book(sender, instance, *args, *kwargs):
    instance.slug = slugify(instance.title)


pre_save.connect(pre_save_book, sender=Book)
