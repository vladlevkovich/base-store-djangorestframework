from rest_framework import serializers
from .models import *


class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('author', 'text', 'product')

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author
        return Comments.objects.create(**validated_data)

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        instance.save()
        return instance


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Comments
        fields = ('author', 'text', 'created', 'children')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'category', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image', 'description', 'comments')


class CartProductSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='id', queryset=Product.objects.all(), required=False)

    class Meta:
        model = CartProduct
        fields = ('product', 'quantity', 'total')


class CartSerializer(serializers.ModelSerializer):
    items = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items')


class CartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'city', 'index', 'total')


class OrderSerializer(serializers.ModelSerializer):
    order = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'order')

