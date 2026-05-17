from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import College, Program, Organization, Student, OrgMember


# ── College ─────────────────────────────────────────────────────────────────

class CollegeListView(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'studentorg/college_list.html'
    paginate_by = 10

class CollegeCreateView(CreateView):
    model = College
    fields = '__all__'
    template_name = 'studentorg/college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    fields = '__all__'
    template_name = 'studentorg/college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'studentorg/college_confirm_delete.html'
    success_url = reverse_lazy('college-list')


# ── Program ──────────────────────────────────────────────────────────────────

class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'studentorg/program_list.html'
    paginate_by = 10

class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'studentorg/program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'studentorg/program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'studentorg/program_confirm_delete.html'
    success_url = reverse_lazy('program-list')


# ── Organization ─────────────────────────────────────────────────────────────

class OrganizationListView(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = 'studentorg/org_list.html'
    paginate_by = 10

class OrganizationCreateView(CreateView):
    model = Organization
    fields = '__all__'
    template_name = 'studentorg/org_form.html'
    success_url = reverse_lazy('org-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    fields = '__all__'
    template_name = 'studentorg/org_form.html'
    success_url = reverse_lazy('org-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'studentorg/org_confirm_delete.html'
    success_url = reverse_lazy('org-list')


# ── Student ──────────────────────────────────────────────────────────────────

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'studentorg/student_list.html'
    paginate_by = 10

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'studentorg/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'studentorg/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'studentorg/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')


# ── OrgMember ────────────────────────────────────────────────────────────────

class OrgMemberListView(ListView):
    model = OrgMember
    context_object_name = 'members'
    template_name = 'studentorg/orgmember_list.html'
    paginate_by = 10

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'studentorg/orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'studentorg/orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'studentorg/orgmember_confirm_delete.html'
    success_url = reverse_lazy('orgmember-list')
