from django.contrib import admin

from .form import BookForm
from .models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = [
        "__unicode__",
        "slug"
    ]
    readonly_fields = ['slug', 'updated', 'timestamp', 'added_by', 'last_edited_by']

    form = BookForm


admin.site.register(Book, BookAdmin)
