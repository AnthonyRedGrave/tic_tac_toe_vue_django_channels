from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'game/list', GameListViewSet)

urlpatterns = [
    path('index/', index, )
]

urlpatterns += router.urls