from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('slack/', include('response.slack.urls')),
    path('core/', include('response.core.urls')),
    path('', include('response.ui.urls')),
]
