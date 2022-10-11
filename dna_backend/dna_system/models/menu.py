from django.db import models
from dna_utils.model import DnaModel


class Menu(DnaModel):
    parent = models.ForeignKey(to="Menu", on_delete=models.CASCADE, null=True, blank=True, db_constraint=False,
                               verbose_name="上级菜单", help_text="上级菜单")
    menu_icon = models.CharField(max_length=64, null=True, blank=True, verbose_name="图标", help_text="图标")
    menu_name = models.CharField(max_length=64, unique=True, verbose_name="菜单name", help_text="菜单name")
    menu_title = models.CharField(max_length=100, verbose_name="菜单名称", help_text="菜单名称")
    menu_path = models.CharField(max_length=255, null=True, blank=True, verbose_name="路由地址", help_text="路由地址")
    component = models.CharField(max_length=255, null=True, blank=True, verbose_name="前端组件", help_text="前端组件")
    is_link = models.BooleanField(default=False, verbose_name="是否外链", help_text="是否外链")
    keep_alive = models.BooleanField(default=False, blank=True, verbose_name="是否页面缓存", help_text="是否页面缓存")
    redirect = models.CharField(max_length=255, null=True, blank=True, verbose_name="重定向地址",
                                help_text="重定向地址")

    class Meta:
        verbose_name = "菜单表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)
