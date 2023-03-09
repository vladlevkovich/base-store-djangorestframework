from django.contrib import admin
from .models import Product, Category, Cart, CartProduct, Comments, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created')
    list_filter = ('id', 'category')
    search_fields = ('id', 'name', 'category')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(CartProduct)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'created')


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')

