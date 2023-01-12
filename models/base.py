from tortoise import fields
from tortoise.models import Model


class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        abstract = True


class FileList(TimestampMixin):
    fid = fields.IntField(pk=True, description='主键id')
    file_id = fields.CharField(max_length=255, null=False, description='文件唯一标识')
    file_name = fields.CharField(max_length=255, null=False, description='文件名')
    file_size = fields.IntField(null=False, description='文件大小')
    file_owner = fields.CharField(max_length=255, null=True, description='文件所有者')
    file_permission = fields.CharField(max_length=255, null=True, description='文件权限')
    file_mime_type = fields.CharField(max_length=255, null=False, description='文件类型')
    file_hash = fields.CharField(max_length=255, null=True, description='文件hash')
    file_is_crypt = fields.BooleanField(null=True, description='文件是否加密')
    file_is_compressed = fields.BooleanField(null=True, description='文件是否压缩')
    file_info = fields.CharField(max_length=255, null=True, description='文件信息')
    file_path = fields.CharField(max_length=255, null=False, description='文件路径')

    class Meta:
        table_description = "文件索引表"
        table = "file_list"


class BlackList(TimestampMixin):
    id = fields.IntField(pk=True, description='主键id')
    ip = fields.CharField(max_length=255, null=False, description='ip地址')
    reason = fields.CharField(max_length=255, null=False, description='原因')
