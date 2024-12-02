from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        # Fetch the object to be deleted
        instance = self.get_object()
        # Serialize the object (for response)
        deleted_data = OrderSerializer(instance).data
        # Delete the object
        self.perform_destroy(instance)
        # Return a detailed response
        return Response(
            {"message": "Order deleted successfully", "order": deleted_data},
            status=status.HTTP_200_OK,
        )
