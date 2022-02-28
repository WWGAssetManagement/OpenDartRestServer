from rest_framework import serializers
from .models import (
    CorpCodeModel,
    DartListModel,
)


class CorpCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorpCodeModel
        fields = (
            'corp_code',
            'corp_name',
            'stock_code'
        )

    stock_code = serializers.CharField(required=False, allow_blank=True)


class DartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DartListModel
        fields = '__all__'
