from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    number_string = models.CharField(verbose_name="Job Number", max_length=140, blank=False, null=False)
    title = models.CharField(verbose_name="Title", max_length=250, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, blank=False, null=False)

    @property
    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.number_string + ": " + self.title
