from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'login', views.Login.as_view())
# router.register(r'sign-up', views.SignUp.as_view())

urlpatterns = [url(r'^', include(router.urls))]

app_name = 'accounts'