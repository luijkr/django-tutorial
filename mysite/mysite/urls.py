from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('polls/', include('polls.urls')),
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
]
