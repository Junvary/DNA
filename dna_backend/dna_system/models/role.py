from django.db import models
from dna_utils.model import DnaModel


class Role(DnaModel):
    role_code = models.CharField(max_length=64, unique=True, verbose_name="角色编码", help_text="角色编码")
    role_name = models.CharField(max_length=64, unique=True, verbose_name="角色名称", help_text="角色名称")
    menu = models.ManyToManyField(to="Menu", db_constraint=False,  verbose_name="关联菜单", help_text="关联菜单")
    api = models.ManyToManyField(to="Api", db_constraint=False, verbose_name="关联Api", help_text="关联Api")

    class Meta:
        verbose_name = "角色表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)
