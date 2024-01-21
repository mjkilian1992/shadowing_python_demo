"""
URL configuration for newsletter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from newsletter import views as index_views

urlpatterns = [
    path("", index_views.HomePageView.as_view(), name="home"),
    path("articles/", index_views.ArticlesView.as_view(), name="articles"),
    path("customer/", include("customer.urls"), name="customer"),
    path("admin/", admin.site.urls),
]
