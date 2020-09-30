from catmaid.control.authentication import requires_user_role as requires_user_role
from django.contrib.auth.decorators import user_passes_test as user_passes_test
from django.http import HttpRequest, JsonResponse
from django.utils.decorators import method_decorator as method_decorator
from rest_framework.views import APIView
from typing import Any

logger: Any

class GroupList(APIView):
    def get(self, request: HttpRequest) -> JsonResponse: ...
