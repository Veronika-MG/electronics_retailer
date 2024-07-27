from django.db import models
from django.utils import timezone
from treebeard.mp_tree import MP_Node


class NetworkNode(MP_Node):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    products = models.ManyToManyField(
        "Product",
        related_name="network_nodes",
        blank=True,
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)

    MAX_NAME_LENGTH = 20

    class Meta:
        verbose_name = "Торговый узел"
        verbose_name_plural = "Торговые Узлы"

    def delete(self, *args, **kwargs):
        children = self.get_children()
        if children:
            parent = self.get_parent()
            if parent:
                for child in children:
                    child.move(parent, pos="last-child")
            else:
                for child in children:
                    child.move(self.get_root(), pos="last-sibling")

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name[: self.MAX_NAME_LENGTH]


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    MAX_LENGTH = 15

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name[:self.MAX_LENGTH]}({self.model[:self.MAX_LENGTH]})"
