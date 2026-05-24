from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import College, Program, Organization, Student, OrgMember
from django.db.models import Q

# ── College ─────────────────────────────────────────────────────────────────

class CollegeListView(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'studentorg/college_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs

    def get_ordering(self):
        allowed = ['prog_name', 'college__college_name', '-prog_name']
        sort_by = self.request.GET.get('sort_by')
        if sort_by in allowed:
            return sort_by
        return 'prog_name'

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(lastname__icontains=query) |
                Q(firstname__icontains=query) |
                Q(student_id__icontains=query)
            )
        return qs

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(student__lastname__icontains=query))
        return qs

    def get_ordering(self):
        allowed = ['student__lastname', 'date_joined', '-date_joined']
        sort_by = self.request.GET.get('sort_by')
        if sort_by in allowed:
            return sort_by
        return '-date_joined'

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
