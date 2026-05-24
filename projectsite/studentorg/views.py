from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import College, Program, Organization, Student, OrgMember
from django.db.models import Q

# ── College ─────────────────────────────────────────────────────────────────

class CollegeListView(LoginRequiredMixin, ListView):
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

class CollegeCreateView(LoginRequiredMixin, CreateView):
    model = College
    fields = '__all__'
    template_name = 'studentorg/college_form.html'
    success_url = reverse_lazy('college-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class CollegeUpdateView(LoginRequiredMixin, UpdateView):
    model = College
    fields = '__all__'
    template_name = 'studentorg/college_form.html'
    success_url = reverse_lazy('college-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class CollegeDeleteView(LoginRequiredMixin, DeleteView):
    model = College
    template_name = 'studentorg/college_confirm_delete.html'
    success_url = reverse_lazy('college-list')


# ── Program ──────────────────────────────────────────────────────────────────

class ProgramListView(LoginRequiredMixin, ListView):
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

class ProgramCreateView(LoginRequiredMixin, CreateView):
    model = Program
    fields = '__all__'
    template_name = 'studentorg/program_form.html'
    success_url = reverse_lazy('program-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'studentorg/program_form.html'
    success_url = reverse_lazy('program-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class ProgramDeleteView(LoginRequiredMixin, DeleteView):
    model = Program
    template_name = 'studentorg/program_confirm_delete.html'
    success_url = reverse_lazy('program-list')


# ── Organization ─────────────────────────────────────────────────────────────

class OrganizationListView(LoginRequiredMixin, ListView):
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

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    fields = '__all__'
    template_name = 'studentorg/org_form.html'
    success_url = reverse_lazy('org-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = '__all__'
    template_name = 'studentorg/org_form.html'
    success_url = reverse_lazy('org-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
    template_name = 'studentorg/org_confirm_delete.html'
    success_url = reverse_lazy('org-list')


# ── Student ──────────────────────────────────────────────────────────────────

class StudentListView(LoginRequiredMixin, ListView):
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

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = '__all__'
    template_name = 'studentorg/student_form.html'
    success_url = reverse_lazy('student-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'studentorg/student_form.html'
    success_url = reverse_lazy('student-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'studentorg/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')


# ── OrgMember ────────────────────────────────────────────────────────────────

class OrgMemberListView(LoginRequiredMixin, ListView):
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

class OrgMemberCreateView(LoginRequiredMixin, CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'studentorg/orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class OrgMemberUpdateView(LoginRequiredMixin, UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'studentorg/orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name_plural
        return context

class OrgMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = OrgMember
    template_name = 'studentorg/orgmember_confirm_delete.html'
    success_url = reverse_lazy('orgmember-list')
