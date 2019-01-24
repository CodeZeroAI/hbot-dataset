from rest_framework import routers

from hbot_dataset.targets.api.viewsets import TargetViewSet
from hbot_dataset.vectors.api.viewsets import TextVectorViewSet

app_name = 'apis'
router = routers.DefaultRouter()
router.register(r'texts', TextVectorViewSet, base_name='text')
router.register(r'targets', TargetViewSet, base_name='target')
urlpatterns = router.urls
