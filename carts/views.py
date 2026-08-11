from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from django.db import transaction
from orders.models import Order, OrderItem
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

    @action(detail=False, methods=['post'], url_path='checkout')
    def checkout(self, request):
        cart = self.get_object()
        cart_items = cart.items.all()

        if not cart_items.exists():
            return Response({'error': 'سبد خرید شما خالی است.'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            product_ids = [item.product_id for item in cart_items]
            products = Product.objects.filter(id__in=product_ids).select_for_update()
            product_dict = {p.id: p for p in products}

            order_items_to_create = []
            order = Order.objects.create(user=request.user)

            for item in cart_items:
                product = product_dict.get(item.product_id)
                if product.inventory < item.quantity:
                    return Response(
                        {'error': f'موجودی محصول {product.name} کافی نیست. موجودی فعلی: {product.inventory}'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                product.inventory -= item.quantity
                product.save()

                order_items_to_create.append(
                    OrderItem(
                        order=order,
                        product=product,
                        quantity=item.quantity,
                        price=product.price
                    )
                )

            OrderItem.objects.bulk_create(order_items_to_create)

            cart_items.delete()

        return Response(
            {'message': 'سفارش با موفقیت ثبت شد.', 'order_id': order.id},
            status=status.HTTP_201_CREATED
        )
    @action(detail=False, methods=['post'], url_path='add-item')
    def add_item(self, request):
        """
        افزودن محصول به سبد خرید یا افزایش تعداد آن در صورت وجود
        """
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({'error': 'product_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)