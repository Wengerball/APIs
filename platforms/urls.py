from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('platforms',views.platformsView)

urlpatterns = [
     url('',include(router.urls))
    #url('', include('platforms.urls'))
]
