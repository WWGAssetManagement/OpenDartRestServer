from django.shortcuts import render
from .serializers import (
    CorpCodeSerializer,
)
from .models import (
    CorpCodeModel,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class CorpCodeView(viewsets.ModelViewSet):
    queryset = CorpCodeModel.objects.all()
    serializer_class = CorpCodeSerializer
