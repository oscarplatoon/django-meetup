from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('groups/', include('meetup_app.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]

handler404 = 'meetup_app.views.error_404_view'
