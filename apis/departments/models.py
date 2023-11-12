from django.db import models
from base.models import BaseModel


class Department(BaseModel):
    name = models.CharField(
        max_length=100
    )
    cost_center = models.CharField(
        max_length=100
    )
    integration_code = models.CharField(
        max_length=100
    )
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.PROTECT,
        related_name='departments'
    )

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return f"Department of {self.name} from {self.company}"
