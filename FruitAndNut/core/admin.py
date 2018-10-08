from django.contrib import admin
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion,Faculty, Testimonial,LabSection


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
    search_fields = ['link_name', 'link']
    list_display = ('link_name', 'link')

    class Meta:
        model = FooterRelatedLinks


class LandingAdmin(admin.ModelAdmin):
    search_fields = ['slider', 'active']
    list_display = ('slider', 'active')

    class Meta:
        model = LandingPortion


class RecentEventAdmin(admin.ModelAdmin):
    search_fields = ['caption', 'date_of_event', 'active']
    list_display = ('caption', 'date_of_event', 'active')

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



admin.site.register(RecentEvent, RecentEventAdmin)
admin.site.register(FooterRelatedLinks, FooterLinkAdmin)
admin.site.register(FooterContact, FooterContactAdmin)
admin.site.register(FooterAbout, FooterContactAdmin)
admin.site.register(LandingPortion, LandingAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(LabSection, LabSectionAdmin)


# admin.site.register()



