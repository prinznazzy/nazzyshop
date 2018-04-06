from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from profiles import views as profiles_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'shopcart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^about/', profiles_views.about, name='about'),
    url(r'^dashboard/', profiles_views.dashboard, name='dashboard'),
    url(r'^shop/',include('shop.urls', namespace='shop')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    # url(r'^happystamp/', include('happystamp.urls')),
    # url(r'^payment/', include('payment.urls', namespace='payment')),
    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
