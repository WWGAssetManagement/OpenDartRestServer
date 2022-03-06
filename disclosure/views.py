from django.shortcuts import render
from .serializers import (
    CorpCodeSerializer,
    DartListSerializer,
)
from .models import (
    CorpCodeModel,
    DartListModel,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .pagination import PostPageNumberPagination

# Create your views here.

class CorpCodeView(viewsets.ModelViewSet):
    queryset = CorpCodeModel.objects.all()
    serializer_class = CorpCodeSerializer
    pagination_class = PostPageNumberPagination


class DartListView(viewsets.ModelViewSet):
    queryset = DartListModel.objects.all()
    serializer_class = DartListSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            headers = self.get_success_headers(data=data)
            serializer.save()
            return Response({
                'response': True,
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response({
            'response': False,
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
