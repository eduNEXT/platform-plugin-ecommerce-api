"""
platform_plugin_ecommerce_api Django application initialization.
"""

from django.apps import AppConfig

class PlatformPluginEcommerceApiConfig(AppConfig):
    """
    Configuration for the platform_plugin_ecommerce_api Django application.
    """

    name = 'platform_plugin_ecommerce_api'
    verbose_name = 'Platform Plugin Ecommerce API'
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'ecommerce-api',
                'regex': r'^ecommerce-api/',
                'relative_path': 'urls',
            }
        },
        
    }
