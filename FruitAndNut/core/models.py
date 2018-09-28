from django.db import models
import datetime as dt

# Create your models here.


class RecentEvent(models.Model):
    description = models.TextField(blank=False)
    date_of_event = models.DateField(default=dt.date.today)
    recent_event_slider = models.ImageField(upload_to='images/recent_event_slider/', unique=True)
    active = models.BooleanField(default=True)
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Recent Event"
        verbose_name_plural = "Recent Events"


class FooterRelatedLinks(models.Model):
    link_name = models.CharField(max_length=30)
    link = models.URLField()

    class Meta:
        verbose_name = "Footer Related Link"
        verbose_name_plural = "Footer Related Links"


    def __str__(self):
        return self.link_name


class FooterAbout(models.Model):
    text_data = models.TextField(blank=True)

    class Meta:
        verbose_name = "Footer About"
        verbose_name_plural = "Footer About"

    def __str__(self):
        return self.text_data


class FooterContact(models.Model):
    text_data = models.TextField(blank=True)

    class Meta:
        verbose_name = "Footer Contact"
        verbose_name_plural = "Footer Contact"

    def __str__(self):
        return self.text_data


class LandingPortion(models.Model):
    slider = models.ImageField(upload_to='images/landing_slider/', unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Landing Portion"
        verbose_name_plural = "Landing Portion"
