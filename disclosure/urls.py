from django.urls import path, include
from .views import (
    CorpCodeView,
    DartListView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('code', CorpCodeView)
router.register('list', DartListView)

urlpatterns = [
    path('company/', include(router.urls)),
    path('', include(router.urls)),
]
