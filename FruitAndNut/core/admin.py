from django.contrib import admin
from . import models


# ------------------------------Common access----------------------------------------

# 1. Footer About
class FooterAboutAdmin(admin.ModelAdmin):
    search_fields = ['text_data']
    list_display = ('text_data',)

    class Meta:
        model = models.FooterAbout


# 2. Footer Contact
class FooterContactAdmin(admin.ModelAdmin):
    search_fields = ['text_data']
    list_display = ('text_data',)

    class Meta:
        model = models.FooterContact


# 3. Footer Link
class FooterLinkAdmin(admin.ModelAdmin):
    search_fields = ['link_name', 'link', 'priority']
    list_display = ('link_name', 'link', 'priority')
    list_display_links = ('link_name', 'link')
    list_editable = ('priority',)
    ordering = ('priority',)

    class Meta:
        model = models.FooterRelatedLinks


# --------------------------------Home Page ----------------------------------

# 1. Landing Page
class LandingAdmin(admin.ModelAdmin):
    search_fields = ['slider', 'active']
    list_display = ('slider', 'active')

    class Meta:
        model = models.LandingPortion


# 2. Recent Event
class RecentEventAdmin(admin.ModelAdmin):
    # search_fields = [ 'event_date', 'active']
    # list_display = ('event_date', 'active')

    class Meta:
        model = models.RecentEvent


# 3. Notification
class NotificationAdmin(admin.ModelAdmin):
    pass


# 4. Quick Links
class QuickLinkAdmin(admin.ModelAdmin):
    pass


# -----------------About ---------------------------------------------------

# 1. Vision and mission
class VisionMissionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = models.VisionAndMission


# 2. Principal
class PrincipalAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = models.Principal


# 3. Infrastructure
class InfrastructureAdmin(admin.ModelAdmin):
    pass


# 4. Faculty
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'designation']
    list_display = ('name', 'designation')

    class Meta:
        model = models.Faculty


# 5. Lab
class LabSectionAdmin(admin.ModelAdmin):
    search_fields = ['lab_name']
    list_display = ('lab_name',)

    class Meta:
        model = models.LabSection


# 6. Gallery
class GalleryAdmin(admin.ModelAdmin):
    pass


# 7. Organization Chart
class OrganizationChartAdmin(admin.ModelAdmin):
    pass


# 8. Important functionary
class ImpFunctionaryAdmin(admin.ModelAdmin):
    search_fields = ['designation', 'name', 'priority']
    list_display = ('designation', 'name', 'priority')
    list_display_links = ('name', 'designation')
    list_editable = ('priority',)
    ordering = ('priority',)

    class Meta:
        model = models.ImportantFunctionary


# -----------------------------ACADEMICS ---------------------------------------

# 1. AffiliationAKTU
class AffiliationAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = models.Affiliation


# 2. Academic awards
class AcademiAwardAdmin(admin.ModelAdmin):
    pass


# 3. Time Table
class TimeTableAdmin(admin.ModelAdmin):
    pass


# 4. Academic Calender
class AcademicCalendarAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = models.AcademicCalendar


# 5. Syllabus
class SyllabusAdmin(admin.ModelAdmin):
    pass


# 6. Old Question Paper
class OldQuestionPaperAdmin(admin.ModelAdmin):
    pass


# --------------------------------R&D-----------------------------------------

# 1. Center of excellence
class CenterOfExcAdmin(admin.ModelAdmin):
    pass


# 2. Research and Industrial Consultancy
class RAICAdmin(admin.ModelAdmin):
    pass


# 3. International Journal
class InternationalJournalAdmin(admin.ModelAdmin):
    pass


# 4. Conferences
class ConferenceAdmin(admin.ModelAdmin):
    pass


# -----------------------------------------Admission----------------------------------

# 1. Admission Process
class AdmissionProcessAdmin(admin.ModelAdmin):
    pass


# 2. Fee structure
class FeeStructureAdmin(admin.ModelAdmin):
    pass


# 3. Refund Norms
class RefundNormAdmin(admin.ModelAdmin):
    pass


# 4. Information Booklet
class InformationBookletAdmin(admin.ModelAdmin):
    pass


# -----------------------------------Placement-----------------------------

# 1. T&P Cell
class TrainingPlacementDepartmentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = models.TrainingPlacementDepartment


# 2. Recruiters
class RecruiterAdmin(admin.ModelAdmin):
    pass


# 3. Placement Records
class PlacementRecordAdmin(admin.ModelAdmin):
    pass


# -----------------Alumni---------------------------------

# 1. Testimonials
class TestimonialAdmin(admin.ModelAdmin):
    search_fields = ['name', 'designation']
    list_display = ('name', 'designation')

    class Meta:
        model = models.Testimonial


# 2. Our Alumni
class OurAlumniAdmin(admin.ModelAdmin):
    pass


# --------------------Life @ AKGEC-MCA --------------------------------------

# 1. Society
class SocietyAdmin(admin.ModelAdmin):
    pass


# 2. Event
class EventAdmin(admin.ModelAdmin):
    pass


# 3. Social Responsibility
class SocialResponsibilityAdmin(admin.ModelAdmin):
    pass


# 4. Hostels
class HostelAdmin(admin.ModelAdmin):
    pass


# 5. Mediclaim
class MediclaimAdmin(admin.ModelAdmin):
    pass


# Common
admin.site.register(models.FooterRelatedLinks, FooterLinkAdmin)
admin.site.register(models.FooterContact, FooterContactAdmin)
admin.site.register(models.FooterAbout, FooterContactAdmin)


# Home
admin.site.register(models.LandingPortion, LandingAdmin)
admin.site.register(models.RecentEvent, RecentEventAdmin)
admin.site.register(models.Notification)


# Quick Links
admin.site.register(models.AicteApprovalLetter),
admin.site.register(models.ListOfHoliday),
admin.site.register(models.MandatoryDisclosure),
admin.site.register(models.Naac),



# About
admin.site.register(models.VisionAndMission, VisionMissionAdmin)
admin.site.register(models.Principal, PrincipalAdmin)
admin.site.register(models.Infrastructure)
admin.site.register(models.Faculty, FacultyAdmin)
admin.site.register(models.LabSection, LabSectionAdmin)
admin.site.register(models.Gallery)
admin.site.register(models.OrganizationChart)
admin.site.register(models.ImportantFunctionary, ImpFunctionaryAdmin)


# Academic
admin.site.register(models.Affiliation, AffiliationAdmin)
admin.site.register(models.UniversityAwards)
admin.site.register(models.CollegeAwards)
admin.site.register(models.TimeTable)
admin.site.register(models.AcademicCalendar, AcademicCalendarAdmin)


# R&D
admin.site.register(models.CenterOfExcellence),
admin.site.register(models.InternationalJournal)
admin.site.register(models.Conference),


# Admission


# Placement
admin.site.register(models.TrainingPlacementDepartment, TrainingPlacementDepartmentAdmin)
admin.site.register(models.Recruiters)
admin.site.register(models.PlacementRecord)


# Alumni
admin.site.register(models.Testimonial, TestimonialAdmin)
admin.site.register(models.OurAlumni)


# Life
admin.site.register(models.Society)
admin.site.register(models.Events)
admin.site.register(models.SocialResponsibility)
admin.site.register(models.Hostel)
admin.site.register(models.Mediclaim)




