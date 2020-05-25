"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from productapp.views import (
        ProductListView,
        ProductDetailView,
        ProductFeaturedListView,
        ProductFeaturedDetailView,
        ProductDetailSlugView
        )

from .views import contact_page, home_page, login_page, register_page

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('products/', include(('productapp.urls','productapp'), namespace='products')),
    path('search/', include(('search.urls','search'), namespace='search')),
    path('carts/', include(('carts.urls','cart'), namespace='cart')),

    path('products/<slug>/', ProductDetailSlugView.as_view()),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('bootstrap',TemplateView.as_view(template_name='bootstrap/example.html'))
    # path('products/<pk>', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<pk>/', ProductFeaturedDetailView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
