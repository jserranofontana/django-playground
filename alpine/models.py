from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)


# From Video 4 Sample
class Course(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")

    def __str__(self):
        return self.name
