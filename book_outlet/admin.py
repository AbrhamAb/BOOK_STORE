from django.contrib import admin
from .models import Author, Book, address, Country
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)

class addressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "state", "zip_code")


class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("author", "rating",)
  list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(address, addressAdmin)
admin.site.register(Country , CountryAdmin)
