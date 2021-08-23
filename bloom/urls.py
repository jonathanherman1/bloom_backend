from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('accounts/signup/', views.signup, name='signup'),
  path('token-auth/', obtain_jwt_token)
]