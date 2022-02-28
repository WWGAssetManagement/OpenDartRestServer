from django.db import models


# Create your models here.
class CorpCodeModel(models.Model):
    corp_code = models.CharField(max_length=10, primary_key=True)
    corp_name = models.CharField(max_length=20, null=True)
    stock_code = models.CharField(max_length=8, null=True)
    modify_date = models.DateField(auto_now_add=True)
