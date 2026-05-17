from django.urls import path
from . import views

urlpatterns = [

    # Colleges
    path('colleges/',           views.CollegeListView.as_view(),   name='college-list'),
    path('colleges/add/',       views.CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<int:pk>/edit/',   views.CollegeUpdateView.as_view(), name='college-edit'),
    path('colleges/<int:pk>/delete/', views.CollegeDeleteView.as_view(), name='college-delete'),

    # Programs
    path('programs/',           views.ProgramListView.as_view(),   name='program-list'),
    path('programs/add/',       views.ProgramCreateView.as_view(), name='program-add'),
    path('programs/<int:pk>/edit/',   views.ProgramUpdateView.as_view(), name='program-edit'),
    path('programs/<int:pk>/delete/', views.ProgramDeleteView.as_view(), name='program-delete'),

    # Organizations
    path('organizations/',           views.OrganizationListView.as_view(),   name='org-list'),
    path('organizations/add/',       views.OrganizationCreateView.as_view(), name='org-add'),
    path('organizations/<int:pk>/edit/',   views.OrganizationUpdateView.as_view(), name='org-edit'),
    path('organizations/<int:pk>/delete/', views.OrganizationDeleteView.as_view(), name='org-delete'),

    # Students
    path('students/',           views.StudentListView.as_view(),   name='student-list'),
    path('students/add/',       views.StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/edit/',   views.StudentUpdateView.as_view(), name='student-edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    # Org Members
    path('members/',           views.OrgMemberListView.as_view(),   name='orgmember-list'),
    path('members/add/',       views.OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('members/<int:pk>/edit/',   views.OrgMemberUpdateView.as_view(), name='orgmember-edit'),
    path('members/<int:pk>/delete/', views.OrgMemberDeleteView.as_view(), name='orgmember-delete'),
]
