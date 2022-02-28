from rest_framework import serializers
from .models import (
    CorpCodeModel
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


