from django.db import models
from base.models import BaseModel


class Employee(BaseModel):
    full_name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        unique=True
    )
    phone_number = models.CharField(
        max_length=20
    )
    birthdate = models.DateField(

    )
    admission_date = models.DateField(

    )
    resignation_date = models.DateField(
        null=True,
        blank=True
    )
    city = models.ForeignKey(
        'base.City',
        on_delete=models.PROTECT,
        related_name='employees'
    )
    department = models.ForeignKey(
        'departments.Department',
        on_delete=models.PROTECT,
        related_name='employees'
    )

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.full_name} - {self.department}"
