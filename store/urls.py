from django.urls import path
from .views import *


urlpatterns = [
    path('products-list/', ProductListView.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    path('category/', CategoryListView.as_view()),

    path('cart-detail/', CartView.as_view()),
    path('add-product-cart/', CartAddProductView.as_view()),
   # path('cart-delete/', CartDeleteView.as_view()),
    path('cart-delete/', CartDeleteView.as_view()),

    path('order/', OrderCreateView.as_view()),

    path('comment/', CreateComment.as_view())
]

