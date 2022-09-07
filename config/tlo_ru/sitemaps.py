from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Product.objects.all()


        
        
# class CategorySitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9

#     def items(self):
#         return Category.published.all()

#     def lastmod(self, obj):
#         return obj.publish
        
        
# class NewsSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9

#     def items(self):
#         return News.published.all()

#     def lastmod(self, obj):
#         return obj.publish
        
        
        
# class ProductSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9

#     def items(self):
#         return Product.published.all()

#     def lastmod(self, obj):
#         return obj.publish

        
# class InfoSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9

#     def items(self):
#         return Info.published.all()

#     def lastmod(self, obj):
#         return obj.publish