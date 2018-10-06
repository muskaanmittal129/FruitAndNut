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


class Faculty(models.Model):
    name = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    profile_pic = models.ImageField(upload_to='images/faculty/', unique=True)
    department = models.CharField(max_length=250, blank=True)
    # date_of_join = models.DateField(blank=False)
    qualification_ug = models.CharField(max_length=250, blank=True )
    qualification_pg = models.CharField(max_length=250, blank= True)
    qualification_phd = models.CharField(max_length=250, blank= True)
    # experience_teaching = models.IntegerField(default=0)
    # experience_industry = models.IntegerField(default=0)
    # experience_research = models.IntegerField(default=0)
    # paper_published_national = models.IntegerField(default=0)
    # paper_published_international = models.IntegerField(default=0)
    # paper_presented_national = models.IntegerField(default=0)
    # paper_presented_international = models.IntegerField(default=0)
    # phd_guide_field = models.TextField(null=True)
    # phd_guide_university = models.TextField(null=True)
    # project_guided_phd = models.TextField(null=True)
    # project_guided_master = models.TextField(null=True)
    # book_published = models.TextField(null=True)
    # professional_membership = models.TextField(null=True)
    # consultancy_activity = models.TextField(null=True)
    # awards = models.TextField(null=True)
    # grants_fetched = models.TextField(null=True)
    # interaction_prof_institution = models.TextField(null=True)

