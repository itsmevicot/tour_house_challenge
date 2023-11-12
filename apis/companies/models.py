from django.db import models
from base.models import BaseModel
from localflavor.br.models import BRCNPJField


class Company(BaseModel):
    name = models.CharField(
        max_length=100
    )
    cnpj = BRCNPJField(
        unique=True
    )
    address = models.CharField(
        max_length=100
    )
    city = models.ForeignKey(
        'base.City',
        on_delete=models.PROTECT,
        related_name='companies'
    )

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
