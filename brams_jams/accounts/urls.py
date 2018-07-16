from rest_framework import routers
from django.conf.urls import url,  include
from .views import SignUp, UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = [ url(r'^', include(router.urls)) ]
# urlpatterns = [
#     url(r'sign-up', SignUp.as_view(), name='sign-up-api'),
# ]

app_name = 'accounts'