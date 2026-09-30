from django.contrib import admin

# Register your models here.
from .models import Author, Book, BookAuthor, BookInstance, Genre, Language

# consider adding save_as to more easily add instance that have similar values
# you could do this for any or all of the below, e.g.
# admin.site.register(Book, save_as=True)
# except mayeb not bookinstance tho

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(BookAuthor)


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1
    fields = ("author", "author_order")


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "date_of_birth",
        "date_of_death",
    )

    fields = [
        "first_name",
        "last_name",
        ("date_of_birth", "date_of_death"),
    ]

    inlines = [BookAuthorInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "display_authors", "display_genre")

    inlines = [BooksInstanceInline, BookAuthorInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id")
    list_filter = ("status", "due_back")

    fieldsets = (
        (
            None,
            {
                "fields": ("book", "imprint", "id"),
            },
        ),
        (
            "Availability",
            {
                "fields": ("status", "due_back"),
            },
        ),
    )
