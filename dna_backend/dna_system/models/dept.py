from django.db import models
from dna_utils.model import DnaModel


class Dept(DnaModel):
    parent = models.ForeignKey(to="Dept", on_delete=models.CASCADE, null=True, blank=True, db_constraint=False,
                               verbose_name="上级部门", help_text="上级部门")
    dept_code = models.CharField(max_length=100, blank=False, null=False, unique=True, verbose_name="部门编码",
                                 help_text="部门编码")
    dept_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="部门名称", help_text="部门名称")
    leader = models.CharField(max_length=32, null=True, blank=True, verbose_name="负责人", help_text="负责人")

    class Meta:
        verbose_name = "部门表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)
