from rest_framework.routers import DefaultRouter
from applications.users.api.views.user_views import UserViewset

router = DefaultRouter()

router.register(r'users',UserViewset,basename='users')


urlpatterns = router.urls