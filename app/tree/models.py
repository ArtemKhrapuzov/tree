from django.db import models
from django.urls import reverse_lazy


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        if self.url_name:
            return reverse_lazy(self.url_name)
        else:
            return self.url