from django.db import models


# Create your models here.
class CorpCodeModel(models.Model):
    """
    OpenDart 회사 코드를 저장을 위한 모델
    """
    corp_code = models.CharField(max_length=10, primary_key=True)
    corp_name = models.CharField(max_length=40, null=True)
    stock_code = models.CharField(max_length=8, null=True)
    add_date = models.DateField(auto_now_add=True)


class DartListModel(models.Model):
    rcept_no = models.CharField(max_length=40, primary_key=True)
    corp_code = models.CharField(max_length=10)
    corp_name = models.CharField(max_length=40, null=True)
    stock_code = models.CharField(max_length=8, null=True)
    corp_cls = models.TextField(null=True)
    report_name = models.CharField(max_length=40, null=True)
    fir_nm = models.CharField(max_length=20, null=True)
    rcept_dt = models.DateTimeField()
    rm = models.CharField(max_length=5, null=True)

