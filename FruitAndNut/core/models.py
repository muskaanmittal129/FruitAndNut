from django.db import models
import datetime as dt

# Create your models here.

class RecentEvent(models.Model):
    description = models.TextField(blank=False)
    date_of_field = models.DateField(default=dt.date.today)


class RecentEventSlider(models.Model):
    recent_event = models.ForeignKey(RecentEvent, on_delete=models.CASCADE)
    recent_event_slider = models.ImageField(upload_to='images/recent_event_slider/', unique=True)
    caption = models.CharField(max_length=200, blank=True)


class FooterRelatedLinks(models.Model):
    link_name = models.CharField(max_length=30)
    link = models.URLField()


class FooterAbout(models.Model):
    text_data = models.TextField(blank=True)


class FooterContact(models.Model):
    text_data = models.TextField(blank=True)

