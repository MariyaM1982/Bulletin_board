from rest_framework.routers import DefaultRouter
from .views import AdViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(r'reviews', ReviewViewSet, basename='review')  # ← basename обязателен!

urlpatterns = router.urls