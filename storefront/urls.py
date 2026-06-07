
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

admin.site.site_header = "Storefront Admin"
admin.site.site_title = "Storefront Admin Portal"
admin.site.index_title = "Welcome to Storefront Admin Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('playground/', include('playground.urls')),
    # path('__debug__/', include(debug_toolbar_urls)),
] + debug_toolbar_urls()
