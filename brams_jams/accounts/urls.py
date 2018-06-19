from rest_framework import routers
from django.conf.urls import url
from .views import SignUp

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'sign-up', SignUp.as_view(), name='sign-up-api'),
]

app_name = 'accounts'