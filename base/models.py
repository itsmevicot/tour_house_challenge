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


# class Country(BaseModel):
#     name = models.CharField(
#         max_length=100
#     )
#     iso3 = models.CharField(
#         max_length=3,
#         null=True,
#         blank=True
#     )
#
#     class Meta:
#         verbose_name = 'Country'
#         verbose_name_plural = 'Countries'
#
#     def __str__(self):
#         return self.name
#
#
# class State(BaseModel):
#     name = models.CharField(
#         max_length=100
#     )
#     country = models.ForeignKey(
#         "base.Country",
#         related_name='states',
#         on_delete=models.PROTECT
#     )
#
#     class Meta:
#         verbose_name = 'State'
#         verbose_name_plural = 'States'
#
#     def __str__(self):
#         return f"{self.name}, {self.country.name}"
#
#
# class City(BaseModel):
#     name = models.CharField(
#         max_length=100
#     )
#     state = models.ForeignKey(
#         "base.State",
#         related_name='cities',
#         on_delete=models.PROTECT
#     )
#     state_code = models.CharField(
#         max_length=3,
#         null=True,
#         blank=True
#     )
#
#     class Meta:
#         verbose_name = 'City'
#         verbose_name_plural = 'Cities'
#
#     def __str__(self):
#         return f"{self.name}, {self.state.name}, {self.state.country.name}"
