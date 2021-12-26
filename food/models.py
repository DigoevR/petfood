from django.db import models
import uuid


class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField(
        max_length=40
    )

    # country = models.ForeignKey(
    #     Country, on_delete=models.SET_NULL, null=true
    # )


class Animal(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField(
        max_length=40
    )


class FoodClass(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField(
        max_length=40
    )


class Package(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    mass = models.DecimalField(
        max_digits=7, decimal_places=3
    )


class Tag(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField(
        max_length=40
    )


class Food(models.Model):
    """#"""
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    name = models.CharField(
        max_length=50, null=False, default='unknown'
    )

    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True
    )

    food_class = models.ForeignKey(
        FoodClass, on_delete=models.SET_NULL, null=True, verbose_name='class of food'
    )

    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, null=True)

    packages = models.ManyToManyField(
        Package, verbose_name='available packages',
        through='FoodPackage', through_fields=('food', 'package')
    )

    # special tags, e.g. for kittens, sterilised cats, animals with diabetes, etc.
    tags = models.ManyToManyField(
        Tag, null=True
    )


class FoodPackage(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    food = models.ForeignKey(
        Food, on_delete=models.CASCADE
    )

    package = models.ForeignKey(
        Package, on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=11, decimal_places=2
    )
