from django.db import models
import psycopg2

class City(models.Model):
    objects = None
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
