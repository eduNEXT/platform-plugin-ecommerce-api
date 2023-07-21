"""
URLs for platform_plugin_ecommerce_api.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from django.urls import path,include
from views import APIConfigView
from django.conf.urls import url

urlpatterns = [
    # other URL patterns for your main app,
    path('api/', include([
        path('user/', APIConfigView.as_view(), name='edxapp-user'),
    ])),
]

