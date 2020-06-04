from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reddit/', include('reddit_app.urls')),
    path('accounts/', include('user_app.urls')),
    path("", include("languagefilter_middleware.urls")),
]
