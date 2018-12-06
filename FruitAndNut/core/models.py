from django.db import models
import datetime as dt
from django.core.validators import RegexValidator

# Create your models here.


class RecentEvent(models.Model):
    description = models.TextField(blank=False)
    date_of_event = models.DateField(default=dt.date.today)
    recent_event_slider = models.ImageField(upload_to='images/recent_event_slider/%Y-%m-%d--%H:%M:%S', unique=True)
    active = models.BooleanField(default=True)
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Recent Event"
        verbose_name_plural = "Recent Events"


class FooterRelatedLinks(models.Model):
    link_name = models.CharField(max_length=30)
    link = models.URLField()
    priority = models.PositiveIntegerField()

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
    slider = models.ImageField(upload_to='images/landing_slider/%Y-%m-%d--%H:%M:%S ', unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Landing Portion"
        verbose_name_plural = "Landing Portion"


class Faculty(models.Model):
    name = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    profile_pic = models.ImageField(upload_to='images/faculty/%Y-%m-%d--%H:%M:%S', unique=True)
    department = models.CharField(max_length=250, blank=True)
    # date_of_join = models.DateField(blank=False)
    qualification_ug = models.CharField(max_length=250, blank=True )
    qualification_pg = models.CharField(max_length=250, blank= True)
    qualification_phd = models.CharField(max_length=250, blank= True)
    faculty_pdf = models.FileField(upload_to='files/faculty_pdf/%Y-%m-%d--%H:%M:%S', unique= True)
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

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class OrganizationChart(models.Model):
    image = models.ImageField(upload_to='images/organization_chart/%Y-%m-%d--%H:%M:%S')

    class Meta:
        verbose_name = "Organization Chart"
        verbose_name_plural = "Organization Chart"


class Gallery(models.Model):
    images = models.ImageField(upload_to='images/gallery/%Y-%m-%d--%H:%M:%S')

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"


class Event(models.Model):
    event_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventImages(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/event/%Y-%m-%d--%H:%M:%S')

    class Meta:
        verbose_name = "Event Image"
        verbose_name_plural = "Event Images"


class ImportantFunctionary(models.Model):
    designation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    telephone_regex = RegexValidator(regex=r'^d{4}([-]*)\d{7}$', message="Format:XXXX-XXXXXXX")
    telephone = models.CharField(validators=[telephone_regex], max_length=12, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number without zero and having 10 numbers")
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    priority = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Important Functionary"
        verbose_name_plural = "Important Functionaries"


class Principal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/principal/%Y-%m-%d--%H:%M:%S')
    messege = models.TextField()


# class Infrastructure(models.Model):
#     image = models.ImageField(upload_to='images/infrastructure%Y-%m-%d--%H:%M:%S')
#     caption = models.CharField(max_length=250)

class Testimonial(models.Model):
    name = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    profile_pic =models.ImageField(upload_to='images/alumni/%Y-%m-%d--%H:%M:%S', unique=True)
    testimonial_message = models.TextField(blank=False)


class LabSection(models.Model):
    lab_name = models.CharField(max_length=250,blank=False)
    image1 = models.ImageField(upload_to='images/labs/%Y-%m-%d--%H:%M:%S', unique=True)
    image2 = models.ImageField(upload_to='images/labs/%Y-%m-%d--%H:%M:%S', unique=True)
    image3 = models.ImageField(upload_to='images/labs/%Y-%m-%d--%H:%M:%S', unique=True)
    lab_description = models.TextField(blank=False)


class Notification(models.Model):
    message = models.TextField()
    active = models.BooleanField(default=False)


