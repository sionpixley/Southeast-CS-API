from django.db import models


class announcement(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    authored_date = models.DateTimeField()
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=400)


class event(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    organization = models.CharField(max_length=100)


class course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()
    prerequisites = models.CharField(max_length=400)
    availability = models.CharField(max_length=400)
    description = models.CharField(max_length=400)


class contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    office = models.CharField(max_length=100)


class admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    passwd = models.CharField(max_length=400)
