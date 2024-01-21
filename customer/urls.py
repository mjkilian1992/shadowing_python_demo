from django.urls import path

from . import views

app_name = "customer"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("thanks/", views.Thanks.as_view(), name="thanks"),
]
