# -*- coding: utf-8 -*-
"""
HOT Exports URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

from api.urls import router
from api.views import request_geonames, get_overpass_timestamp
from ui.views import (
    about, create_error_view, help_create, help_exports, help_features,
    help_formats, help_main, help_presets, login, logout, require_email,
    v3, help_feature_selections
)

admin.autodiscover()

urlpatterns = []

urlpatterns += i18n_patterns(
    url(r'^$', login, name='index'),
    url(r'^v3/$', v3, name="v3"),
    url(r'^login/$', login, name="login"),
    url(r'^logout$', logout, name='logout'),
    url(r'^error$', create_error_view, name='error'),
    url(r'^about$', about, name='about'),
    url(r'^update$', TemplateView.as_view(
        template_name='ui/upgrade.html'), name='update'),
    url(r'^email/$', require_email, name='require_email'),
)

urlpatterns += i18n_patterns(
    url(r'^help$', help_main, name='help'),
    url(r'^help/create$', help_create, name='help_create'),
    url(r'^help/features$', help_features, name='help_features'),
    url(r'^help/exports$', help_exports, name='help_exports'),
    url(r'^help/formats$', help_formats, name='help_formats'),
    url(r'^help/presets$', help_presets, name='help_presets'),
    url(r'^help/feature_selections$', help_feature_selections, name='help_feature_selections'),
)

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
)

# OAuth client urls
urlpatterns += i18n_patterns(
    url('^osm/', include('social_django.urls', namespace='osm')),
    url('^osm/email_verify_sent/$', TemplateView.as_view(
        template_name='osm/email_verify_sent.html'), name='email_verify_sent'),
    url('^osm/error$', TemplateView.as_view(template_name='osm/error.html'),
        name='login_error')
)

# OAuth provider urls
urlpatterns += [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

# don't apply i18n patterns here.. api uses Accept-Language header
urlpatterns += [
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^request_geonames$', login_required(request_geonames)),
    url(r'^api/overpass_timestamp$', login_required(get_overpass_timestamp))
]

# i18n for js
js_info_dict = {
    'packages': ('hot_osm',),
}

urlpatterns += [
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['hot_osm']), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

# handler500 = 'ui.views.internal_error_view'

# handler404 = 'ui.views.not_found_error_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
