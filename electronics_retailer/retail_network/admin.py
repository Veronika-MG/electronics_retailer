from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from retail_network import services
from retail_network.models import NetworkNode, Product


@admin.register(NetworkNode)
class MyAdmin(TreeAdmin):
    list_display = (
        "short_name",
        "id",
        "email",
        "address",
        "level",
        "debt",
    )
    list_filter = ("city", "country")
    search_fields = ("name", "id")

    def short_name(self, obj):
        if len(obj.name) > obj.MAX_NAME_LENGTH:
            return obj.name[: obj.MAX_NAME_LENGTH] + "..."
        return obj.name

    short_name.short_description = "Name"

    def level(self, obj):
        return services.get_node_level(obj)

    def address(self, obj):
        return f"{obj.country} {obj.city} {obj.street}, {obj.house_number}"

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
    actions = [clear_debt]
    form = movenodeform_factory(NetworkNode)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "model", "release_date")
    search_fields = ("name", "model")
    list_filter = ("release_date",)
