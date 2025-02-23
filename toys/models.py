from django.db import models

class CapsuleToy(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # ← これを追加！

    def __str__(self):
        return self.name
