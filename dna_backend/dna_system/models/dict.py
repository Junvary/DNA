from django.db import models
from dna_utils.model import DnaModel


class Dict(DnaModel):
    parent = models.ForeignKey(to="Dict", on_delete=models.CASCADE, null=True, blank=True, db_constraint=False,
                               verbose_name="上级字典", help_text="上级字典")
    dict_value = models.CharField(max_length=64, unique=True, verbose_name="字典编码", help_text="字典编码")
    dict_label = models.CharField(max_length=64, unique=True, verbose_name="字典名称", help_text="字典名称")
    ext1 = models.CharField(max_length=64, verbose_name="字典扩展1", help_text="字典扩展1")
    ext2 = models.CharField(max_length=64, verbose_name="字典扩展2", help_text="字典扩展2")
    ext3 = models.CharField(max_length=64, verbose_name="字典扩展3", help_text="字典扩展3")
    ext4 = models.CharField(max_length=64, verbose_name="字典扩展4", help_text="字典扩展4")
    ext5 = models.CharField(max_length=64, verbose_name="字典扩展5", help_text="字典扩展5")

    class Meta:
        verbose_name = "字典表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)
