from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import InventoryItem

from .serializers import InventoryItemSerializer

class InventoryItemViewSet(ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def destroy(self, request, *args, **kwargs):
        # Fetch the object to be deleted
        instance = self.get_object()
        # Serialize the object (for response)
        deleted_data = InventoryItemSerializer(instance).data
        # Delete the object
        self.perform_destroy(instance)
        # Return a detailed response
        return Response(
            {"message": "Invebtory deleted successfully", "inventory": deleted_data},
            status=status.HTTP_200_OK,
        )
