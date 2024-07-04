from django.contrib import admin
from django.urls import path, include

from newsletter.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
]
