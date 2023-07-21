from django.conf import settings
from django.http import HttpResponseNotFound, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers

class APIConfigView(request):
    
    def get(self, request):


        return JsonResponse({"mensaje":"test success"}, status=status.HTTP_200_OK)