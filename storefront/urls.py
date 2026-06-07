
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('playground/', include('playground.urls')),
    # path('__debug__/', include(debug_toolbar_urls)),
] + debug_toolbar_urls()
