from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class College(BaseModel):
    college_name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.college_name

    class Meta:
        ordering = ['college_name']
        verbose_name = "College"
        verbose_name_plural = "Colleges"


class Program(BaseModel):
    prog_name = models.CharField(max_length=150)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return self.prog_name

    class Meta:
        ordering = ['prog_name']
        verbose_name = "Program"
        verbose_name_plural = "Programs"


class Organization(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    college = models.ForeignKey(College, null=True, blank=True, on_delete=models.SET_NULL, related_name='organizations')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


class Student(BaseModel):
    student_id = models.CharField(max_length=15, unique=True)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

    def get_full_name(self):
        parts = [self.firstname]
        if self.middlename:
            parts.append(self.middlename[0] + '.')
        parts.append(self.lastname)
        return ' '.join(parts)

    class Meta:
        ordering = ['lastname', 'firstname']
        verbose_name = "Student"
        verbose_name_plural = "Students"


class OrgMember(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='memberships')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.student} — {self.organization}"

    class Meta:
        ordering = ['-date_joined']
        verbose_name = "Organization Member"
        verbose_name_plural = "Organization Members"
        unique_together = ('student', 'organization')
