from django.db import models


class ActiveManager(models.Manager):
    def actives(self, **kwargs):
        """
        Returns a queryset containing all instances of the model where 'is_active' is True.
        Raises a ValueError if 'active' is provided as a keyword argument.
        """
        if 'is_active' in kwargs:
            raise ValueError('Cannot override the value of "is_active" in actives.')
        return self.get_queryset().filter(is_active=True, **kwargs)

    def inactives(self, **kwargs):
        """
        Returns a queryset containing all instances of the model where 'is_active' is False.
        Raises a ValueError if 'active' is provided as a keyword argument.
        """
        if 'is_active' in kwargs:
            raise ValueError('Cannot override the value of "is_active" in inactives.')
        return self.get_queryset().filter(is_active=False, **kwargs)
