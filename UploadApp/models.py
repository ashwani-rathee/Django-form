from django.db import models

class Course(models.Model):
    image = models.ImageField(upload_to='images/')
