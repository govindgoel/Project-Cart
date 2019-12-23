from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView

app_name = 'shop'

urlpatterns = [
    url('product/register/', views.registerView, name="register_urls"),
    url('product/login', LoginView.as_view(), name="login_url"),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]