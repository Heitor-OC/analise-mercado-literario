from django_mongoengine import mongo_admin as admin
from .models import Category, Book

@admin.register(Category)
class CategoryAdmin(admin.DocumentAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.DocumentAdmin):
    pass
