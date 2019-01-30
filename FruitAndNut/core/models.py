from django.db import models
import datetime as dt
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

year_dropdown = []
for y in range(2011, (datetime.datetime.now().year + 5)):
    y= str(y)+'-'+str(y+1)
    year_dropdown.append((y, y))

# Create your models here.


class RecentEvent(models.Model):
    description = models.TextField(blank=False)
    date_of_event = models.DateField(default=dt.date.today)
    recent_event_slider = models.ImageField(upload_to='images/recent_event_slider/%Y-%m-%d', unique=True)
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
    slider = models.ImageField(upload_to='images/landing_slider/%Y-%m-%d', unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Landing Portion"
        verbose_name_plural = "Landing Portion"


class Faculty(models.Model):
    name = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    profile_pic = models.ImageField(upload_to='images/faculty/%Y-%m-%d', unique=True)
    department = models.CharField(max_length=250, blank=True)
    # date_of_join = models.DateField(blank=False)
    qualification_ug = models.CharField(max_length=250, blank=True )
    qualification_pg = models.CharField(max_length=250, blank= True)
    qualification_phd = models.CharField(max_length=250, blank= True)
    faculty_pdf = models.FileField(upload_to='files/faculty_pdf/%Y-%m-%d', unique= True)
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
    image = models.ImageField(upload_to='images/organization_chart/%Y-%m-%d')

    class Meta:
        verbose_name = "Organization Chart"
        verbose_name_plural = "Organization Chart"

    def __str__(self):
        return self.image


class Gallery(models.Model):
    images = models.ImageField(upload_to='images/gallery/%Y-%m-%d')

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.images


class Event(models.Model):
    event_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event_name


class EventImages(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/event/%Y-%m-%d')

    class Meta:
        verbose_name = "Event Image"
        verbose_name_plural = "Event Images"

    def __str__(self):
        return self.event


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
    image = models.ImageField(upload_to='images/principal')
    message = RichTextUploadingField()

    class Meta:
        verbose_name = 'Principal'
        verbose_name_plural = 'Prinicipal'

    def __str__(self):
        return self.name


class Infrastructure(models.Model):
    image = models.ImageField(upload_to='images/infrastructure')
    caption = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Infrastructure"
        verbose_name_plural = 'Infrastructure'


class LabSection(models.Model):
    lab_name = models.CharField(max_length=250,blank=False)
    image1 = models.ImageField(upload_to='images/labs/%Y-%m-%d', unique=True)
    image2 = models.ImageField(upload_to='images/labs/%Y-%m-%d', unique=True)
    image3 = models.ImageField(upload_to='images/labs/%Y-%m-%d', unique=True)
    lab_description = models.TextField(blank=False)

    def __str__(self):
        return self.lab_name

    class Meta:
        verbose_name = "Lab Section"
        verbose_name_plural = 'Lab Section'


class Notification(models.Model):
    message = models.TextField()
    link = models.URLField(max_length=250, blank= True)
    file = models.FileField(upload_to='files/notification//%Y-%m-%d', blank=True )
    active = models.BooleanField(default=False)

    def __str__(self):
        if len(self.message) > 20:
            return self.message[0:20]
        return self.message

    def clean(self):
        if not self.link and not self.file:
            raise ValidationError({'Add at least one field '})
        elif self.link and self.file:
            raise ValidationError({'Either add link or add file'})


class VisionAndMission(models.Model):
    vision = RichTextUploadingField()
    mission = RichTextUploadingField()
    policy = RichTextUploadingField()

    class Meta:
        verbose_name = 'Vision And Mission'
        verbose_name_plural = "Vision And Mission"

    def __str__(self):
        return "Vision And Mission"


# ------------------- R && D models -----------------

class Conference(models.Model):
    title = models.CharField(max_length=250, blank=False)
    cover_photo = models.ImageField(upload_to='images/conference/%Y-%m-%d')
    content = models.FileField(upload_to='files/conference/%Y-%m-%d')

    def __str__(self):
        return self.title


class CenterOfExcellence(models.Model):
    logo = models.ImageField(upload_to='images/center_of_excellence/%Y-%m-%d')
    title = models.CharField(max_length=250, blank=False)
    content = models.TextField(blank=False)
    website_link = models.URLField(max_length=250)

    class Meta:
        verbose_name = 'Center Of Excellence'
        verbose_name_plural = "Center Of Excellence"

    def __str__(self):
        return self.title


class ResearchAndIndustrial(models.Model):
    content = RichTextUploadingField()


class InternationalJournal(models.Model):
    content = RichTextUploadingField()

# ---------------------- Quick link ----------------------------------


class ListOfHoliday(models.Model):
    content = models.ImageField(upload_to='images/list_of_holidays/%Y-%m-%d')

    class Meta:
        verbose_name = 'List Of Holiday'
        verbose_name_plural = "List Of Holidays"

    def __str__(self):
        return "List-Of-Holidays"


class Naac(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.FileField(upload_to='files/naac/%Y-%m-%d')

    class Meta:
        verbose_name = 'NAAC'
        verbose_name_plural = "NAAC"

    def __str__(self):
        return self.title


class AicteApprovalLetter(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.FileField(upload_to='files/aicte_approval_letter/%Y-%m-%d')

    class Meta:
        verbose_name = 'AICTE Approval Letter'
        verbose_name_plural = "AICTE Approval Letters"

    def __str__(self):
        return self.title


class MandatoryDisclosure(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.FileField(upload_to='files/mandatory_disclosure/%Y-%m-%d')

    class Meta:
        verbose_name = 'Mandatory Disclosure'
        verbose_name_plural = "Mandatory Disclosure"

    def __str__(self):
        return self.title


class Download(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.FileField(upload_to='files/download/%Y-%m-%d')

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = "Downloads"

    def __str__(self):
        return self.title

# ---------------------  end of Quick Link models ---------------------

# ---------------------  start of Admission Models --------------------


class FeeStructure(models.Model):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = 'Fee Structure'
        verbose_name_plural = "Fee Structure"

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


class AdmissionProcess(models.Model):
    content = RichTextUploadingField()


class InfoBooklet(models.Model):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = 'Information Booklet'
        verbose_name_plural = "Information Booklet"

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


class RefundNorm(models.Model):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = 'Refund Norm'
        verbose_name_plural = "Refund Norm"

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


# ---------------------  end of Admission Models --------------------

# ---------------------  end of Life-akgec-mca Models --------------------


class Events(models.Model):
    image = models.ImageField(upload_to='images/events/%Y-%m-%d')
    content = models.TextField()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


class Hostel(models.Model):
    image = models.ImageField(upload_to='images/hostel/%Y-%m-%d')
    content = models.TextField()

    class Meta:
        verbose_name = 'Hostel'
        verbose_name_plural = 'Hostel'

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


class SocialResponsibility(models.Model):
    image = models.ImageField(upload_to='images/social_responsibility/%Y-%m-%d')
    content = models.TextField()

    class Meta:
        verbose_name = 'Social Responsibility'
        verbose_name_plural = 'Social Responsibility'

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


class Society(models.Model):
    image = models.ImageField(upload_to='images/social_responsibility/%Y-%m-%d')
    content = models.TextField()

    class Meta:
        verbose_name = 'Society'
        verbose_name_plural = 'Society'

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


class Mediclaim(models.Model):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = 'Mediclaim'
        verbose_name_plural = 'Mediclaim'

    def __str__(self):
        if len(self.content) > 20:
            return self.content[0:20]
        return self.content


# ---------------------  end of life-akgec-mca Models --------------------#

# ----------------------academic section--------------------------------#

class Affiliation(models.Model):
    affiliation_image= models.ImageField(upload_to='images/affiliation')

    class Meta:
        verbose_name = 'Affiliation'
        verbose_name_plural = 'Affiliation'


class AcademicCalendar(models.Model):
    image = models.ImageField(upload_to='images/calendar/%Y-%m-%d')

    class Meta:
        verbose_name = 'AcademicCalendar'
        verbose_name_plural = 'AcademicCalendar'


class TimeTable(models.Model):
    year = models.IntegerField()
    section = models.IntegerField()
    image = models.ImageField(upload_to='images/timetable/%Y-%m-%d')

    class Meta:
        verbose_name = 'Time Table'
        verbose_name_plural = 'Time Tables'


class UniversityAwards(models.Model):
    session = models.CharField(('year'), choices=year_dropdown, default=datetime.datetime.now().year, max_length=10)
    name = models.CharField(max_length=255)
    univ_position = models.IntegerField()
    percentage_marks = models.DecimalField(max_digits=6, decimal_places=3)
    medal = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'University Award'
        verbose_name_plural = 'University Awards'


class CollegeAwards(models.Model):
    session = models.CharField(('year'),choices=year_dropdown, default=datetime.datetime.now().year, max_length=10)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    percentage_marks = models.DecimalField(max_digits=6, decimal_places=3)

    class Meta:
        verbose_name = 'College Award'
        verbose_name_plural = 'College Awards'


# ----------------------------start of placement section-------------------#


class TrainingPlacementDepartment(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/placement')
    message = RichTextUploadingField()


    class Meta:
        verbose_name = 'T & P Department'
        verbose_name_plural = 'T & P Department'

    def __str__(self):
        return self.name


class Recruiters(models.Model):
    image = models.ImageField(upload_to='images/placement')

    class Meta:
        verbose_name = 'Recruiters'
        verbose_name_plural = 'Recruiters'


class PlacementRecord(models.Model):
    image = models.ImageField(upload_to='images/placement')

    class Meta:
        verbose_name = 'Placement Record'
        verbose_name_plural = 'Placement Record'

# ------------------ TrainingPlacementDepartment ends ----------------------------#

# -------------------alumni section starts-----------------------#


class Testimonial(models.Model):
    name = models.CharField(max_length=250, blank=False)
    designation = models.CharField(max_length=250, blank=False)
    profile_pic = models.ImageField(upload_to='images/testimonial/%Y-%m-%d', unique=True)
    testimonial_message = models.TextField(blank=False)

    class Meta:
        verbose_name = 'Testimonial '
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class OurAlumni(models.Model):
    name= models.CharField(max_length=250, blank= False)
    profile_pic = models.ImageField(upload_to='images/alumni/%Y-%m-%d')
    email =  models.EmailField(blank=True)
    phone_contact = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Our Alumni '
        verbose_name_plural = 'Our Alumni'

# ---------------------------alumni section ends-----------------------#

