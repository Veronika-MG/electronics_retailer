from django.urls import include, path
from rest_framework.routers import DefaultRouter

from retail_network.views import NetworkNodeViewSet

router = DefaultRouter()
router.register(r"networknodes", NetworkNodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
