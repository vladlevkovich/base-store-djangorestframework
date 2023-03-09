from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework import permissions
from .models import Product, Category
from .serializers import *


class ProductListView(generics.ListAPIView):
    """Product list"""
    queryset = Product.objects.filter(availability=True)
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartView(generics.RetrieveAPIView):
    """Creates a shopping cart for user if it does not exist otherwise displays a cart """
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)
        return cart


class CartAddProductView(generics.CreateAPIView):
    """This class fills the cart with goods"""
    serializer_class = CartProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity')
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_product.quantity += quantity
            cart_product.save()
        else:
            cart_product.quantity = quantity
            cart_product.total = product.price * quantity
            cart_product.save()
        cart.total += cart_product.total
        cart.save()


class CartUpdateView(generics.UpdateAPIView):
    """Class updates the contents of the cart"""
    serializer_class = CartProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart = Cart.objects.get(user=self.request.user)
        return cart

    def put(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CartDeleteView(generics.DestroyAPIView):
    """Class deleted cart"""
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        try:
            cart = Cart.objects.get(user=user)
            cart.delete()
        except:
            return None

        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateComment(views.APIView):
    """Add a comment to the product"""
    serializer_class = AddCommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('REQUEST: ', serializer.errors)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CreateOrder(generics.CreateAPIView):
    """Creates an order"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_object(self):
        user = self.request.user
        try:
            order = Order.objects.get(user=user)
            return order
        except Order.DoesNotExist:
            order = Order.objects.create(user=user)
            return order


class OrderCreateView(generics.CreateAPIView):
    """Placing an order"""
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        total_price = cart.total
        city = serializer.validated_data.get('city')
        index = serializer.validated_data.get('index')
        order = Order.objects.create(user=user, total=total_price)
        order_item, create = OrderItem.objects.get_or_create(
            order=order,
            cart=cart,
            city=city,
            index=index,
            total=total_price
        )
        order.save()
        order_item.save()



