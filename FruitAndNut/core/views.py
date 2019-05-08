from django.shortcuts import render
from django.views import generic
from . import models
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion, Faculty,Testimonial,\
    LabSection, ImportantFunctionary, Gallery, Event, EventImages\
    , OrganizationChart, Principal, VisionAndMission,\
    Infrastructure, AcademicCalendar, TimeTable, Affiliation, UniversityAwards, TrainingPlacementDepartment, \
    Recruiters, PlacementRecord, OurAlumni


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

    def __init__(self):
        self.context.update(get_footer())
        self.get_recent_event()
        self.get_landing_porting()
        self.get_notification()

    def get_recent_event(self):
        self.context["event_info"] = RecentEvent.objects.filter(active=True)

    def get_landing_porting(self):
        self.context["landing_portion"] = LandingPortion.objects.filter(active=True)

    def get_notification(self):
        self.context["notify_active"] = models.Notification.objects.filter(active=True)
        self.context["notify_not_active"] = models.Notification.objects.filter(active=False)

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


# ----------------    start about page urls  ----------------------

class FacultyView(generic.ListView):
    template_name = 'core/about/faculty.htm'
    context ={}

    def __init__(self):
        self.context.update(get_footer())
        self.get_faculty()

    def get_faculty(self):
        faculty_info = Faculty.objects.all()
        self.context['faculty_info'] = faculty_info

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class LabView(generic.ListView):
    template_name = 'core/about/Labs.htm'
    context ={}

    def __init__(self):
        self.context.update(get_footer())
        self.get_lab()

    def get_lab(self):
        lab_info = LabSection.objects.all()
        self.context['lab_info'] = lab_info

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class GalleryView(generic.ListView):
    template_name = 'core/about/gallery.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_gallery()

    def get_gallery(self):
        gallery_info = Gallery.objects.all()
        self.context['gallery_info'] = gallery_info

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


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

    def __init__(self):
        self.context.update(get_footer())
        self.get_imp_functionary()

    def get_imp_functionary(self):
        imp_functionary = ImportantFunctionary.objects.order_by('priority')
        self.context['imp_functionaries'] = imp_functionary

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class OrganizationChartView(generic.ListView):
    template_name = 'core/about/organization_chart.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_organization_chart()

    def get_organization_chart(self):
        try:
            organization_chart = OrganizationChart.objects.all()[0]
        except:
            organization_chart = None
        self.context['organization_chart'] = organization_chart

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class PrincipalView(generic.ListView):
    template_name = 'core/about/principal.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_principal()

    def get_principal(self):
        try:
            principal = Principal.objects.all()[0]
        except:
            principal = None
        self.context['principal'] = principal

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class VisionMissionView(generic.ListView):
    template_name = 'core/about/vision_and_mission.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_content()

    def get_content(self):
        content = VisionAndMission.objects.all()
        self.context['content'] = content

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class FacultyIncentiveView(generic.ListView):
    template_name = 'core/about/faculty_incentives.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class InfrastructureView(generic.ListView):
    template_name = 'core/about/infrastructure.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_infrastructure()

    def get_infrastructure(self):
        infra_info = Infrastructure.objects.all()
        self.context['infra_info'] = infra_info

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


# --------------------end of about page views -------------------------

# ---------------------- academics views start ----------------------


class AffiliationView(generic.ListView):
    template_name = 'core/academic/affiliation.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_affiliation()

    def get_affiliation(self):
        affiliation = Affiliation.objects.all()
        self.context['affiliation'] = affiliation

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class TimeTableView(generic.ListView):
    template_name = 'core/academic/time_table.html'
    context = {}
    context.update(get_footer())

    def __init__(self):
        self.context.update(get_footer())
        self.get_timetable()

    def get_timetable(self):
        timetable = TimeTable.objects.all()
        self.context['timetable'] = timetable

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class AcademicCalendarView(generic.ListView):
    template_name = 'core/academic/calender.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_calender()

    def get_calender(self):
        calender_info = AcademicCalendar.objects.all()
        self.context['calender_info'] = calender_info

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class SyllabusView(generic.ListView):
    template_name = 'core/academic/syllabus.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class UniversityAwardsYearView(generic.ListView):
    template_name = 'core/academic/awards_list.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context['uni_award_list'] = models.UniversityAwards.objects.values('session').distinct()
        return render(self.request, self.template_name, self.context)


class CollegeAwardsYearView(generic.ListView):
    template_name = 'core/academic/college_award_year.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context['colg_award_list'] = models.CollegeAwards.objects.values('session').distinct()
        return render(self.request, self.template_name, self.context)


class CollegeAwardsView(generic.DetailView):
    template_name = 'core/academic/college_awards.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        session = kwargs['session']
        print(session)
        college_awards_info = models.CollegeAwards.objects.filter(session=session)
        self.context['college_awards_info'] = college_awards_info
        return render(self.request, self.template_name, self.context)


class UniversityAwardsView(generic.ListView):
    template_name = 'core/academic/university_awards.html'
    context ={}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        session = kwargs['session']
        print(session)
        univ_awards_info = models.UniversityAwards.objects.filter(session =session)
        self.context['univ_awards_info'] = univ_awards_info
        print(univ_awards_info)
        return render(self.request, self.template_name, self.context)


class CollegeAwardView(generic.ListView):
    template_name = 'core/academic/college_awards.html'
    context ={}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        session = kwargs['session']
        print(session)
        colg_awards_info = models.CollegeAwards.objects.filter(session = session)
        self.context['colg_awards_info'] = colg_awards_info
        return render(self.request, self.template_name, self.context)


# ----------------------end of academic view --------------------

# ---------------------start of end of r_and_d -----------------


class CenterOfExcView(generic.ListView):
    template_name = 'core/r_and_d/center_of_exc.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["center_of_exc"] = models.CenterOfExcellence.objects.all()
        return render(self.request, self.template_name, self.context)


class ConferencesView(generic.ListView):
    template_name = 'core/r_and_d/conferences.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["conferences"] = models.Conference.objects.all()
        return render(self.request, self.template_name, self.context)


class InternationalJournalView(generic.ListView):
    template_name = 'core/r_and_d/international_journal.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["inter_journal"] = models.InternationalJournal.objects.all().first()
        return render(self.request, self.template_name, self.context)


class ResearchAndIndustrialView(generic.ListView):
    template_name = 'core/r_and_d/research_and_industrial.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["ricc"] = models.ResearchAndIndustrial.objects.all()
        return render(self.request, self.template_name, self.context)


# ---------------------- end of r_and_d ---------------------------

# ---------------------- start of placement views ---------------------------

class PlacementRecordView(generic.ListView):
    template_name = 'core/placement/placement_record.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context['placement_record'] = PlacementRecord.objects.all()
        return render(self.request, self.template_name, self.context)


class RecruiterView(generic.ListView):
    template_name = 'core/placement/recruitors.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context['recruiters_info'] = Recruiters.objects.all()
        return render(self.request, self.template_name, self.context)


class TrainingPlacemenTDepartmentView(generic.ListView):
    template_name = 'core/placement/tnp_cell.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context['TNP_info'] = TrainingPlacementDepartment.objects.all()
        return render(self.request, self.template_name, self.context)


# ---------------------- end of placement views ---------------------------

# ---------------------- start of life akgec-mca views ---------------------------


class EventView(generic.ListView):
    template_name = 'core/life_akgec/event.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["events"] = models.Events.objects.all()
        return render(self.request, self.template_name, self.context)


class HostelView(generic.ListView):
    template_name = 'core/life_akgec/hostel.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["hostel"] = models.Hostel.objects.all()
        return render(self.request, self.template_name, self.context)


class MediclaimView(generic.ListView):
    template_name = 'core/life_akgec/mediclaim.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["medicliam"] = models.Mediclaim.objects.all()
        return render(self.request, self.template_name, self.context)


class SocialResponsibilityView(generic.ListView):
    template_name = 'core/life_akgec/social_responsibility.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["social_responsibility"] = models.SocialResponsibility.objects.all()
        return render(self.request, self.template_name, self.context)


class SocietyView(generic.ListView):
    template_name = 'core/life_akgec/society.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["society"] = models.Society.objects.all()
        return render(self.request, self.template_name, self.context)

# ---------------------- end of life akgec-mca views ---------------------------

# ---------------------- start of alumni views ---------------------------


class TestimonialView(generic.ListView):
    template_name = 'core/alumni/testimonial.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())
        self.get_testimonial()

    def get_testimonial(self):
        testimonial_info = Testimonial.objects.all()
        self.context['testimonial_info'] = testimonial_info

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class AlumniView(generic.ListView):
    template_name = 'core/alumni/our_alumni.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get_alumni(self):
        alumni_info = OurAlumni.objects.all()
        self.context['alumni_info'] = alumni_info

    def get(self, request, *args, **kwargs):
        self.get_alumni()
        return render(self.request, self.template_name, self.context)

# ---------------------- end of alumni views ---------------------------


# ---------------------- start of admission views ---------------------------

class AdmissionProcessView(generic.ListView):
    template_name = 'core/admission/admission_process.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.context)


class FeeStructureView(generic.ListView):
    template_name = 'core/admission/fee_structure.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["fee_structure"] = models.FeeStructure.objects.all()
        return render(self.request, self.template_name, self.context)


class InfoBookletView(generic.ListView):
    template_name = 'core/admission/info_booklet.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["info_booklet"] = models.InfoBooklet.objects.all()
        return render(self.request, self.template_name, self.context)


class RefundNormsView(generic.ListView):
    template_name = 'core/admission/refund_norms.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["refund_norms"] = models.RefundNorm.objects.all()
        return render(self.request, self.template_name, self.context)


# ---------------------- end of admission views ---------------------------


# ---------------------- start of Quick Links views ---------------------------

class DownloadView(generic.ListView):
    template_name = 'core/quick_link/download.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["downloads"] = models.Download.objects.all()
        return render(self.request, self.template_name, self.context)


class AicteApprovalLetterView(generic.ListView):
    template_name = 'core/quick_link/aicte_approval_letter.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["aicte"] = models.AicteApprovalLetter.objects.all()
        return render(self.request, self.template_name, self.context)


class ListOfHolidayView(generic.ListView):
    template_name = 'core/quick_link/list_of_holiday.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["list_of_holidays"] = models.ListOfHoliday.objects.all()
        return render(self.request, self.template_name, self.context)


class NaacView(generic.ListView):
    template_name = 'core/quick_link/naac.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["naac"] = models.Naac.objects.all()
        return render(self.request, self.template_name, self.context)


class MandatoryDisclosureView(generic.ListView):
    template_name = 'core/quick_link/mandatory_disclosure.html'
    context = {}

    def __init__(self):
        self.context.update(get_footer())

    def get(self, request, *args, **kwargs):
        self.context["mandatory_disclosure"] = models.MandatoryDisclosure.objects.all()
        return render(self.request, self.template_name, self.context)

# ---------------------- end of quick links views ---------------------------

