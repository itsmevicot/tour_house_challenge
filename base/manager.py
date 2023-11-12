from django.db import models


class ActiveManager(models.Manager):
    def actives(self, **kwargs):
        """
        Returns a queryset containing all instances of the model where 'active' is True.
        Raises a ValueError if 'active' is provided as a keyword argument.
        """
        if 'active' in kwargs:
            raise ValueError('Cannot override the value of "active" in actives.')
        return self.get_queryset().filter(active=True, **kwargs)

    def inactives(self, **kwargs):
        """
        Returns a queryset containing all instances of the model where 'active' is False.
        Raises a ValueError if 'active' is provided as a keyword argument.
        """
        if 'active' in kwargs:
            raise ValueError('Cannot override the value of "active" in inactives.')
        return self.get_queryset().filter(active=False, **kwargs)
