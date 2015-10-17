from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    lat = models.FloatField(default=44.475833)
    lon = models.FloatField(default=-73.211944)
    imagelink = models.URLField(max_length=200,default="http://newbreedmarketing.com")
    location = models.CharField(max_length=200,default="Burlington, VT")
    name = models.CharField(max_length=200,default="Andy Reagan")
    company = models.TextField(default="",null=True,blank=True)
    description = models.TextField(default="Something about Andy")
    client = models.ForeignKey(User,related_name="cities",null=True)

    def __unicode__(self):
        return self.location

# Store the markup surrounding the map
class Markup(models.Model):
    before = models.TextField()
    inbetween = models.TextField()
    after = models.TextField()
    jscode = models.TextField()
    client = models.ForeignKey(User,related_name="markupcode",null=True)
    def __unicode__(self):
        return self.client.username
