from rest_framework import routers
from .views import DirectorViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'directores', DirectorViewSet)
router.register(r'peliculas', MovieViewSet)

urlpatterns = router.urls