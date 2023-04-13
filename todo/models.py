from django.db import models

# Create your models here.


# Class inheritance from Django's built-in Model class
class Item(models.Model):
    # Define the attribute that our 'items' will have
    # Django creates the id field automatically
    # Defensive restrictions added as args
    name = models.CharField(max_length=50, null=False, blank=False)
    is_done = models.BooleanField(default=False, null=False, blank=False)

    # Override default Django behaviour of displaying:
    # class.name, 'object', (class.pk)
    def __str__(self):
        return self.name
