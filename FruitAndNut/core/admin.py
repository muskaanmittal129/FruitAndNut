from django.contrib import admin
from . import models
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion,Faculty,Testimonial,LabSection, \
    Principal, OrganizationChart, Gallery, Event, ImportantFunctionary, VisionAndMission, Infrastructure, \
    AcademicCalendar, Affiliation, Awards, UniversityAwards, TrainingPlacementDepartment, Recruiters, PlacementRecord,\
    OurAlumni


class FooterAboutAdmin(admin.ModelAdmin):
    search_fields = ['text_data']
    list_display = ('text_data',)

    class Meta:
        model = FooterAbout


class FooterContactAdmin(admin.ModelAdmin):
    search_fields = ['text_data']
    list_display = ('text_data',)

    class Meta:
        model = FooterContact


class FooterLinkAdmin(admin.ModelAdmin):
    search_fields = ['link_name', 'link', 'priority']
    list_display = ('link_name', 'link', 'priority')
    list_display_links = ('link_name', 'link')
    list_editable = ('priority',)
    ordering = ('priority',)
    class Meta:
        model = FooterRelatedLinks


class LandingAdmin(admin.ModelAdmin):
    search_fields = ['slider', 'active']
    list_display = ('slider', 'active')

    class Meta:
        model = LandingPortion


class RecentEventAdmin(admin.ModelAdmin):
    # search_fields = [ 'event_date', 'active']
    # list_display = ('event_date', 'active')

    class Meta:
        model = RecentEvent


class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['name','designation']
    list_display =  ('name','designation')

    class Meta:
        model = Faculty


class TestimonialAdmin(admin.ModelAdmin):
    search_fields = ['name','designation']
    list_display =  ('name','designation')

    class Meta:
        model = Testimonial


class LabSectionAdmin(admin.ModelAdmin):
    search_fields = ['lab_name']
    list_display = ('lab_name',)

    class Meta:
        model = LabSection

class LAdmin(admin.ModelAdmin):
    search_fields = ['lab_name']
    list_display = ('lab_name',)

    class Meta:
        model = LabSection


class ImpFunctionaryAdmin(admin.ModelAdmin):
    search_fields = ['designation', 'name', 'priority']
    list_display = ('designation', 'name', 'priority')
    list_display_links = ('name', 'designation')
    list_editable = ('priority',)
    ordering = ('priority',)

    class Meta:
        model = ImportantFunctionary


class VisionMissionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = VisionAndMission


class PrincipalAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = Principal


class AcademicCalendarAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    class Meta:
        model = AcademicCalendar


admin.site.register(RecentEvent, RecentEventAdmin)
admin.site.register(FooterRelatedLinks, FooterLinkAdmin)
admin.site.register(FooterContact, FooterContactAdmin)
admin.site.register(FooterAbout, FooterContactAdmin)
admin.site.register(LandingPortion, LandingAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(LabSection, LabSectionAdmin)
admin.site.register(VisionAndMission, VisionMissionAdmin)
admin.site.register(Principal, PrincipalAdmin)
admin.site.register(Gallery)
admin.site.register(OrganizationChart)
admin.site.register(Infrastructure)
admin.site.register(ImportantFunctionary, ImpFunctionaryAdmin)
admin.site.register(models.Conference),
admin.site.register(models.CenterOfExcellence),
admin.site.register(models.AicteApprovalLetter),
admin.site.register(models.ListOfHoliday),
admin.site.register(models.MandatoryDisclosure),
admin.site.register(models.Events)
admin.site.register(models.Hostel)
admin.site.register(models.Mediclaim)
admin.site.register(models.SocialResponsibility)
admin.site.register(models.Society)
admin.site.register(models.AcademicCalendar, AcademicCalendarAdmin)
admin.site.register(models.TimeTable)
admin.site.register(models.Affiliation)
admin.site.register(models.Awards)
admin.site.register(models.UniversityAwards)
admin.site.register(models.CollegeAwards)
admin.site.register(models.TrainingPlacementDepartment)
admin.site.register(models.Recruiters)
admin.site.register(models.PlacementRecord)
admin.site.register(models.OurAlumni)





