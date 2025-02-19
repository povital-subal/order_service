from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .grpc_client import fetch_user_details

class OrderListCreate(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        order_total = request.data.get('order_total')

        user_data = fetch_user_details(user_id)
        if not user_data:
            return Response({"error": "User not found"}, status=404)

        order = Order.objects.create(user_id=user_id, order_total=order_total)
        serializer = OrderSerializer(order)
        return Response({
            "order": serializer.data,
            "user": user_data
        })
