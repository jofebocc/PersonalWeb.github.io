from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField(max_length=1000)
    image = models.ImageField(max_length=264,upload_to="projects")
    information = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title