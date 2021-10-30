from django.contrib import admin
from .models import Product, Category, Comment, Contact


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "person",
        "product",
        "body",
        "posted_at",
    ]
    readonly_fields = [
        "posted_at",
    ]
    

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'person',
        'email',
        'inquiry',
        'time',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)