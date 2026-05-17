from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from studentorg.models import College, Program, Organization, Student, OrgMember


class HomeView(TemplateView):
    template_name = 'studentorg/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['college_count'] = College.objects.count()
        ctx['program_count'] = Program.objects.count()
        ctx['org_count']     = Organization.objects.count()
        ctx['student_count'] = Student.objects.count()
        ctx['recent_orgs']   = Organization.objects.select_related('college')[:5]
        ctx['recent_members']= OrgMember.objects.select_related('student','organization')[:5]
        return ctx


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('studentorg.urls')),
]
