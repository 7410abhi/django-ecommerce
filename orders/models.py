from django.db import models

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define the primary key
    user_id = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=[
            ("created", "Created"),
            ("shipped", "Shipped"),
            ("delivered", "Delivered"),
        ],
        default="created",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
