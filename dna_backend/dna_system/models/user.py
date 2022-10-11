from django.db import models
from django.contrib.auth.models import AbstractUser
from dna_utils.model import DnaModel

GenderOptions = (
    (0, "保密"),
    (1, "男"),
    (2, "女"),
)


class User(DnaModel, AbstractUser):
    username = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="用户账号",
                                help_text="用户账号")
    nickname = models.CharField(max_length=150, blank=True, verbose_name="用户昵称", help_text="用户昵称")
    real_name = models.CharField(max_length=150, blank=True, verbose_name="真实姓名", help_text="真实姓名")
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name="电话", help_text="电话")
    avatar = models.CharField(max_length=255, null=True, blank=True, verbose_name="头像", help_text="头像")
    gender = models.IntegerField(choices=GenderOptions, default=0, null=True, blank=True, verbose_name="性别",
                                 help_text="性别")
    role = models.ManyToManyField(to="Role", blank=True, db_constraint=False, verbose_name="关联角色",
                                  help_text="关联角色")
    dept = models.ForeignKey(to="Dept", null=True, blank=True, db_constraint=False, on_delete=models.PROTECT)

    class Meta(AbstractUser.Meta):
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ("username",)
