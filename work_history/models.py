from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    company = models.CharField(max_length=64)
    business_unit = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    start_date = models.CharField(max_length=8)
    end_date = models.CharField(max_length=8)
    summary = models.CharField(max_length=512)


class Education(models.Model):
    institution = models.CharField(max_length=32)
    degree = models.CharField(max_length=32)
    summary = models.CharField(max_length=128)


class Skills(model.Model):
    category = models.CharField(max_length=16)
    summary = models.CharField(max_length=32)