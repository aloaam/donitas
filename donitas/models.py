from django.db import models


# Create your models here.
class Dona(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
