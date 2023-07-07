from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializers


class CreateOrderView(ListCreateAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        order = user.orders.all()
        serializer = serializers.OrderSerializer(order, many=True)
        return Response(serializer.data, status=200)
