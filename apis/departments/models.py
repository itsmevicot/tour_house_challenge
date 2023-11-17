from django.db import models
from base.models import BaseModel


class Department(BaseModel):
    name = models.CharField(
        max_length=100
    )
    cost_center = models.CharField(
        max_length=10,
        unique=True
    )
    integration_code = models.CharField(
        max_length=10,
        unique=True
    )
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.PROTECT,
        related_name='departments'
    )

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        unique_together = ['name', 'company']

    def __str__(self):
        return f"Department of {self.name} from {self.company}"
