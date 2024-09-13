import uuid
from django.db.models import UUIDField, DateTimeField, Model
from django.contrib.auth.models import AbstractUser

class UUIDMixin(Model):
    id = UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )

    class Meta:
        abstract = True


class TimestampMixin(Model):
    created_at = DateTimeField(auto_now_add=True)
    edited_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True