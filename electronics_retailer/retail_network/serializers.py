from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from retail_network import services

from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    level = SerializerMethodField(read_only=True)

    class Meta:
        model = NetworkNode
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "level",
        ]

    def get_level(self, obj):
        return services.get_node_level(obj)


class ProductField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        serializer = ProductSerializer(value)
        return dict(serializer.data)


class NetworkNodeSerializer(serializers.ModelSerializer):
    level = SerializerMethodField(read_only=True)
    products = ProductField(many=True, queryset=Product.objects.all())
    supplier = SerializerMethodField(read_only=True)
    debt = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
        coerce_to_string=False,
    )
    supplier_id = serializers.IntegerField(
        required=False,
        allow_null=True,
        write_only=True,
    )

    def get_supplier(self, obj):
        parent = obj.get_parent()
        if parent:
            parent_node = obj.get_parent()
            return dict(SupplierSerializer(parent_node).data)
        return None

    def get_level(self, obj):
        return services.get_node_level(obj)

    class Meta:
        model = NetworkNode
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "debt",
            "products",
            "level",
            "created_at",
            "supplier",
            "supplier_id",
        ]

    def create(self, validated_data):
        parent_id = validated_data.pop("supplier_id", None)
        products = validated_data.pop("products", None)

        if NetworkNode.objects.filter(id=parent_id).exists():
            parent = NetworkNode.objects.get(id=parent_id)
            instance = parent.add_child(**validated_data)
        elif parent_id == 0 or not parent_id:
            instance = NetworkNode.add_root(**validated_data)
        else:
            raise serializers.ValidationError(
                {"detail": f"Поставщика с id {parent_id} не существует"},
            )

        if products:
            instance.products.set(products)
        return instance
