from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static

from tlo_ru.sitemaps import *

app_name = 'tlo_ru'



sitemaps = {
    # 'sliders': SliderSitemap,
    # 'categoies': CategorySitemap,
    # 'news': NewsSitemap,
    'products': ProductSitemap,
    # 'info':InfoSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tlo_ru.urls')),
    # path('eng/', include('tlo_eng.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)