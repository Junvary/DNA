from django.db import models
from dna_utils.model import DnaModel


class Api(DnaModel):
    api_group = models.CharField(max_length=100, verbose_name="api分组", help_text="api分组")
    api_method = models.CharField(max_length=10, verbose_name="api方法", help_text="api方法")
    api_path = models.CharField(max_length=150, verbose_name="api路径", help_text="api路径")

    class Meta:
        verbose_name = "Api表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)
