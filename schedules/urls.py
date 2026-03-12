from rest_framework.routers import DefaultRouter
from .views import WorkingHoursViewSet

router = DefaultRouter()
router.register(r'working-hours', WorkingHoursViewSet)

urlpatterns = router.urls