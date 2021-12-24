from django.db import models
import uuid


class Food(models.Model):
    """#"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    brand = models.ForeignKey(Brand, on_delete=models.cascade())
    # price
    # food_type
    # animal
    # price
