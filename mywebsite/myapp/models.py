from django.db import models
from datetime import datetime
# Create your models here.


class Contact_Us_Form(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.Name