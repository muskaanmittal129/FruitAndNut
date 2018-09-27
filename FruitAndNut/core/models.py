from django.db import models
import datetime as dt

# Create your models here.


class RecentEvent(models.Model):
    description = models.TextField(blank=False)
    date_of_event = models.DateField(default=dt.date.today)
    recent_event_slider = models.ImageField(upload_to='images/recent_event_slider/', unique=True)
    active = models.BooleanField(default=True)
    caption = models.CharField(max_length=200, blank=True)


class FooterRelatedLinks(models.Model):
    link_name = models.CharField(max_length=30)
    link = models.URLField()


class FooterAbout(models.Model):
    text_data = models.TextField(blank=True)


class FooterContact(models.Model):
    text_data = models.TextField(blank=True)


class LandingPortion(models.Model):
    slider = models.ImageField(upload_to='images/landing_slider/', unique=True)
    active = models.BooleanField(default=True)

