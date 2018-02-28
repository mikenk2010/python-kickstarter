from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView

from dashboard.views import DashboardTemplateView, MyView, BookDetail

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    # url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^book/(?P<slug>[-\w]+)$', BookDetail.as_view(), name='book_detail'),
    url(r'^someview/$', MyView.as_view(template_name='about.html'), name='about'),
    url(r'^about/$', DashboardTemplateView.as_view(), name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
