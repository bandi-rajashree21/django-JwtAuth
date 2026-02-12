from django.shortcuts import render
from django.template.context_processors import request

from config.app.views import HelloView
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, Rajashree'}
        return Response(content)
    