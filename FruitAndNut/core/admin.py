from django.contrib import admin
from .models import RecentEvent, FooterAbout, FooterContact, FooterRelatedLinks, LandingPortion


admin.site.register(RecentEvent)
admin.site.register(FooterRelatedLinks)
admin.site.register(FooterContact)
admin.site.register(FooterAbout)
admin.site.register(LandingPortion)

# admin.site.register()



