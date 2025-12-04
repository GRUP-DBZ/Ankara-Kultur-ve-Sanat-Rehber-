from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} - {self.city}"
