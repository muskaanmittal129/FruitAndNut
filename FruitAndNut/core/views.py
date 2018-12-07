from django.shortcuts import render
from django.views import generic
from . import models
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion, Faculty,Testimonial,\
    LabSection, ImportantFunctionary, Gallery, Event, EventImages, OrganizationChart, Principal, VisionAndMission,\
    Infrastructure


def get_footer_about():
    context = {}
    context["footer_about"] = FooterAbout.objects.all().first()
    return context


def get_footer_contact():
    context = {}
    contact_list = [contact.text_data for contact in FooterContact.objects.all()]
    context["footer_contact"] = contact_list
    return context


def get_footer_related_links():
    context = {}
    context["footer_related_links"] = FooterRelatedLinks.objects.order_by('priority')
    return context


def get_footer():
    context={}
    context.update(get_footer_about())
    context.update(get_footer_related_links())
    context.update(get_footer_contact())
    return context

# home page views


class Home(generic.DetailView):
    template_name = 'core/home/home.html'
    context = {}
    context.update(get_footer())

    def get_recent_event(self):
        self.context["event_info"] = RecentEvent.objects.filter(active=True)

    def get_landing_porting(self):
        self.context["landing_portion"] = LandingPortion.objects.filter(active=True)

    def get_notification(self):
        self.context["notification"] = models.Notification.objects.all()

    def get(self, *args, **kwargs):
        self.get_recent_event()
        self.get_landing_porting()
        self.get_notification()
        return render(self.request, self.template_name, self.context)


# ----------------    start about page urls  ----------------------

class FacultyView(generic.ListView):
    template_name = 'core/about/faculty.htm'
    context ={}
    context.update(get_footer())

    def get_faculty(self):
        faculty_info = Faculty.objects.all()
        self.context['faculty_info'] = faculty_info

    def get(self, request, *args, **kwargs):
        self.get_faculty()
        return render(self.request,self.template_name,self.context)


class LabView(generic.ListView):
    template_name = 'core/about/Labs.htm'
    context ={}
    context.update(get_footer())

    def get_lab(self):
        lab_info = LabSection.objects.all()
        self.context['lab_info'] = lab_info

    def get(self, *args, **kwargs):
        self.get_lab()
        return render(self.request,self.template_name, self.context)


class GalleryView(generic.ListView):
    template_name = 'core/about/gallery.html'
    context = {}
    context.update(get_footer())

    def get_gallery(self):
        gallery_info = Gallery.objects.all()
        self.context['gallery_info'] = gallery_info

    def get(self, request, *args, **kwargs):
        self.get_gallery()
        return render(self.request,self.template_name)


# class RecentEventView(generic.ListView):
#     template_name = 'core/recent_events.html'
#     context ={}
#
#     def get_event(self):
#         event_info = RecentEvent.objects.filter(active=True)
#         self.context['event_info'] = event_info
#
#     def get(self, request, *args, **kwargs):
#         self.get_event()
#         return render(self.request,self.template_name,self.context)

class ImportantFunctionaryView(generic.ListView):
    template_name = 'core/about/important_functionary.html'
    context = {}
    context.update(get_footer())

    def get_imp_functionary(self):
        imp_functionary = ImportantFunctionary.objects.order_by('priority')
        self.context['imp_functionaries'] = imp_functionary

    def get(self, request, *args, **kwargs):
        self.get_imp_functionary()
        return render(self.request,self.template_name,self.context)


class OrganizationChartView(generic.ListView):
    template_name = 'core/about/organization_chart.html'
    context = {}
    context.update(get_footer())

    def get_organization_chart(self):
        try:
            organization_chart = OrganizationChart.objects.all()[0]
        except:
            organization_chart = None
        self.context['organization_chart'] =  organization_chart

    def get(self, request, *args, **kwargs):
        self.get_organization_chart()
        return render(self.request,self.template_name,self.context)


class PrincipalView(generic.ListView):
    template_name = 'core/about/principal.html'
    context = {}
    context.update(get_footer())

    def get_principal(self):
        try:
            principal = Principal.objects.all()[0]
        except:
            principal = None
        self.context['principal'] = principal

    def get(self, request, *args, **kwargs):
        self.get_principal()
        return render(self.request, self.template_name, self.context)


class VisionMissionView(generic.ListView):
    template_name = 'core/about/vision_and_mission.html'
    context = {}
    context.update(get_footer())

    def get_content(self):
        content = VisionAndMission.objects.all()
        self.context['content'] = content

    def get(self, request, *args, **kwargs):
        self.get_content()
        return render(self.request, self.template_name, self.context)


class FacultyIncentiveView(generic.ListView):
    template_name = 'core/about/faculty_incentives.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class InfrastructureView(generic.ListView):
    template_name = 'core/about/infrastructure.html'
    context = {}
    context.update(get_footer())

    def get_infrastructure(self):
        infra_info = Infrastructure.objects.all()
        self.context['infra_info'] = infra_info

    def get(self, request, *args, **kwargs):
        self.get_infrastructure()
        return render(self.request, self.template_name, self.context)


# --------------------end of about page views -------------------------

# ---------------------- academics views start ----------------------

class TimeTableView(generic.ListView):
    template_name = 'core/academic/time_table.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class AcademicCalenderView(generic.ListView):
    template_name = 'core/academic/calender.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class SyllabusView(generic.ListView):
    template_name = 'core/academic/syllabus.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

# ----------------------end of academic view --------------------

# ---------------------start of end of r_and_d -----------------


class CenterOfExcView(generic.ListView):
    template_name = 'core/r_and_d/center_of_exc.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class ConferencesView(generic.ListView):
    template_name = 'core/r_and_d/conferences.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class InternationalJournalView(generic.ListView):
    template_name = 'core/r_and_d/international_journal.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class ResearchAndIndustrialView(generic.ListView):
    template_name = 'core/r_and_d/research_and_industrial.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


# ---------------------- end of r_and_d ---------------------------

# ---------------------- start of placement views ---------------------------

class PlacementRecordView(generic.ListView):
    template_name = 'core/placement/placement_record.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class RecruitorView(generic.ListView):
    template_name = 'core/placement/recruitors.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class TNPCellView(generic.ListView):
    template_name = 'core/placement/tnp_cell.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


# ---------------------- end of placement views ---------------------------

# ---------------------- start of life akgec-mca views ---------------------------


class EventView(generic.ListView):
    template_name = 'core/life_akgec/event.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class HostelView(generic.ListView):
    template_name = 'core/life_akgec/hostel.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class MediclaimView(generic.ListView):
    template_name = 'core/life_akgec/mediclaim.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class SocialResponsibilityView(generic.ListView):
    template_name = 'core/life_akgec/social_responsibility.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class SocietyView(generic.ListView):
    template_name = 'core/life_akgec/society.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

# ---------------------- end of life akgec-mca views ---------------------------

# ---------------------- start of alumni views ---------------------------


class AlumniView(generic.ListView):
    template_name = 'core/alumni/testimonial.html'
    context = {}
    context.update(get_footer())

    def get_testimonial(self):
        testimonial_info = Testimonial.objects.all()
        self.context['testimonial_info'] = testimonial_info

    def get(self, request, *args, **kwargs):
        self.get_testimonial()
        return render(self.request,self.template_name,self.context)

# ---------------------- end of alumni views ---------------------------


# ---------------------- start of admission views ---------------------------

class AdmissionProcessView(generic.ListView):
    template_name = 'core/admission/admission_process.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class FeeStructureView(generic.ListView):
    template_name = 'core/admission/fee_structure.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class InfoBookletView(generic.ListView):
    template_name = 'core/admission/info_booklet.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class RefundNormsView(generic.ListView):
    template_name = 'core/admission/refund_norms.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)



# ---------------------- end of admission views ---------------------------


# ---------------------- start of Quick Links views ---------------------------


class DownloadView(generic.ListView):
    template_name = 'core/quick_link/download.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class AicteApprovalLetterView(generic.ListView):
    template_name = 'core/quick_link/aicte_approval_letter.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class ListOfHolidayView(generic.ListView):
    template_name = 'core/quick_link/list_of_holiday.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class NaacView(generic.ListView):
    template_name = 'core/quick_link/naac.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class MandatoryDisclosureView(generic.ListView):
    template_name = 'core/quick_link/mandatory_disclosure.html'
    context = {}
    context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)

# ---------------------- end of quick links views ---------------------------

