"""
URL configuration for hello_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from core import views          # Forma 2 de fazer
from core.views import hello    # Forma 1 de fazer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/<nome>/<int:idade>", hello, name="hello"),        # Forma 1 de fazer
    path("soma/<int:n1>/<int:n2>/", views.soma),                  # Forma 2 de fazer
    path("subtraction/<int:n1>/<int:n2>/", views.subtraction),    # Forma 2 de fazer
    path("multiply/<int:n1>/<int:n2>/", views.multiply),
    path("divisor/<str:n1>/<str:n2>/", views.divisor, name="divisor"),
]
