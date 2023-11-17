from django.db import models
from base.manager import ActiveManager


class BaseModel(models.Model):
    """
    A base model that includes a created_at and updated_at timestamp and an active boolean. It also includes a custom
    delete method that sets active to False instead of actually deleting the object.
    """
    objects = ActiveManager()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True, editable=False)

    class Meta:
        abstract = True

    def delete(self):
        self.is_active = False
        self.save()
