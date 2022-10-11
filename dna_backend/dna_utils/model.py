from django.db import models
from django.conf import settings


class DnaModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="Id", verbose_name="Id")
    sort = models.IntegerField(default=0, verbose_name="排序", help_text="排序")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="创建时间",
                                     verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="修改时间",
                                     verbose_name="修改时间")
    create_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name="create_by_user", null=True,
                                  blank=True, on_delete=models.SET_NULL, db_constraint=False, verbose_name='创建人',
                                  help_text="创建人")
    update_by = models.CharField(max_length=255, null=True, blank=True, help_text="修改人", verbose_name="修改人")
    is_active = models.BooleanField(default=True, null=False, blank=False, help_text="是否激活",
                                    verbose_name="是否激活")
    memo = models.TextField(null=True, blank=True, verbose_name="备注", help_text="备注")

    class Meta:
        abstract = True
        verbose_name = 'DNA模型基本扩展'
        verbose_name_plural = verbose_name
