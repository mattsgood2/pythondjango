from django.db import models

# Create your models here.

class Film(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=100)
    release_year = models.CharField(max_length=10)

    def __str__(self):
        return ('{} : {}'.format(self.title, self.description))
