from django.db import models

class InventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
