from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from newsletter.views import HomePageView

urlpatterns = [
                  path('', HomePageView.as_view(), name='home'),
                  path('admin/', admin.site.urls),
                  path('newsletter/', include('newsletter.urls', namespace='newsletter')),
                  path('accounts/', include('django.contrib.auth.urls')),
              ]
