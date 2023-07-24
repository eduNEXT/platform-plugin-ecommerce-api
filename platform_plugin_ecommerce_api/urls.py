"""
URLs for platform_plugin_ecommerce_api.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from django.urls import path,include
from platform_plugin_ecommerce_api.views import CourseEnrollmentView
from django.conf.urls import url

urlpatterns = [
    url(r'^enrollment/$', CourseEnrollmentView.as_view(), name='enrollment'),
]

