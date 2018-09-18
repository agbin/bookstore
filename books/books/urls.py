"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.urlpatterns import format_suffix_patterns

from bookshop.views import IndexView, CategoryView, CategoryCreate, ProductsView, \
    ProductCreate, ProductUpdate, CategoryUpdate, BookShopView, BookView, Product_detail, \
    ProductDelete, Login, Logout, Search, signup, Authors_list, Authors_products, AuthorCreate, AuthorUpdate




urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^categories/(?P<slug>(\w|\W+\d+)+)/$', CategoryView.as_view(), name='category'),
    url(r'^category/add/$', CategoryCreate.as_view(), name='category-add'),
    url(r'^category/update/(?P<slug>(\w|\W+\d+)+)/$', CategoryUpdate.as_view(), name='category-update'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^product/(?P<pk>[0-9]+)/$', Product_detail.as_view(), name='detail'),
    url(r'^product/update/(?P<pk>[0-9]+)/$', ProductUpdate.as_view(), name='product-update'),
    url(r'^product/delete/(?P<pk>[0-9]+)/$', ProductDelete.as_view(), name='product-delete'),
    url(r'^product/add/$', ProductCreate.as_view(), name='product-add'),
    url(r'^books/$', BookShopView.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', BookView.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('search/', Search.as_view(), name='search'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^authors/$', Authors_list.as_view(), name='author-list'),
    url(r'^authors/(?P<id>[0-9]+)/$', Authors_products.as_view(), name='authors-products'),
    url(r'^author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'^author/update/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
