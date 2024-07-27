from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import NetworkNode
from .serializers import NetworkNodeSerializer


class IsActiveUser(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filtr_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["country"]
    search_fields = ["name", "email", "city", "street"]
    permission_classes = [IsActiveUser]

    def get_queryset(self):
        country = self.request.query_params.get("country", None)
        if country is not None:
            return self.queryset.filter(country=country)
        return self.queryset
