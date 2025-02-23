from django.db import models

from django.db import models

class CapsuleToy(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)  # ここを修正（必須を解除）
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
