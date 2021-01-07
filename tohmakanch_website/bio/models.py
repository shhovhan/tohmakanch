from django.db import models


class Biography(models.Model):
    author_name = models.CharField(max_length=55)
    bio = models.TextField()

    class Meta:
        db_table='biography'
        verbose_name = 'Biography'

    def __str__(self):
        return self.author_name