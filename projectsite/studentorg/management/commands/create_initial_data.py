from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember
from datetime import date


class Command(BaseCommand):
    help = 'Seed the database with initial PSUSphere data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Seeding database...'))
        self.create_colleges()
        self.create_programs()
        self.create_organizations()
        self.create_students()
        self.create_memberships()
        self.create_fake_students(50)
        self.create_fake_memberships(20)
        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))

    # ── Real seed data ──────────────────────────────────────────────

    def create_colleges(self):
        colleges = [
            "College of Computer Studies",
            "College of Engineering",
            "College of Business Administration",
            "College of Education",
            "College of Arts and Sciences",
            "College of Nursing",
            "College of Hospitality Management",
            "College of Criminology",
        ]
        for name in colleges:
            College.objects.get_or_create(college_name=name)
        self.stdout.write(self.style.SUCCESS(f'  → {len(colleges)} colleges created'))

    def create_programs(self):
        programs = [
            ("BS Computer Science",          "College of Computer Studies"),
            ("BS Information Technology",    "College of Computer Studies"),
            ("BS Software Engineering",      "College of Computer Studies"),
            ("BS Civil Engineering",         "College of Engineering"),
            ("BS Mechanical Engineering",    "College of Engineering"),
            ("BS Business Administration",   "College of Business Administration"),
            ("BS Accountancy",               "College of Business Administration"),
            ("Bachelor of Secondary Education", "College of Education"),
            ("BS Psychology",                "College of Arts and Sciences"),
            ("BS Nursing",                   "College of Nursing"),
        ]
        for prog_name, college_name in programs:
            college = College.objects.get(college_name=college_name)
            Program.objects.get_or_create(prog_name=prog_name, defaults={'college': college})
        self.stdout.write(self.style.SUCCESS(f'  → {len(programs)} programs created'))

    def create_organizations(self):
        ccs = College.objects.get(college_name="College of Computer Studies")
        orgs = [
            {
                "name": "ACS",
                "college": ccs,
                "description": "Association of Computer Students — fostering excellence in computing and technology.",
            },
            {
                "name": "SITE",
                "college": ccs,
                "description": "Society of Information Technology Enthusiasts — driving innovation in IT.",
            },
        ]
        for org in orgs:
            Organization.objects.get_or_create(name=org["name"], defaults={
                "college": org["college"],
                "description": org["description"],
            })
        self.stdout.write(self.style.SUCCESS(f'  → {len(orgs)} organizations created'))

    def create_students(self):
        program = Program.objects.get(prog_name="BS Information Technology")
        students = [
            {
                "student_id": "2023-1-0001",
                "lastname": "Avanceña",
                "firstname": "Gabriel",
                "middlename": "",
                "program": program,
            },
        ]
        for s in students:
            Student.objects.get_or_create(student_id=s["student_id"], defaults=s)
        self.stdout.write(self.style.SUCCESS(f'  → {len(students)} real student(s) created'))

    def create_memberships(self):
        gabriel = Student.objects.get(student_id="2023-1-0001")
        site    = Organization.objects.get(name="SITE")
        OrgMember.objects.get_or_create(
            student=gabriel,
            organization=site,
            defaults={"date_joined": date(2024, 6, 1)},
        )
        self.stdout.write(self.style.SUCCESS('  → 1 real membership created'))

    # ── Fake data ───────────────────────────────────────────────────

    def create_fake_students(self, count):
        fake = Faker('en_PH')
        programs = list(Program.objects.all())
        created = 0
        attempts = 0
        while created < count and attempts < count * 3:
            attempts += 1
            sid = f"{fake.random_int(2020,2025)}-{fake.random_int(1,8)}-{fake.random_number(digits=4, fix_len=True)}"
            if Student.objects.filter(student_id=sid).exists():
                continue
            Student.objects.create(
                student_id=sid,
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=fake.random_element(programs),
            )
            created += 1
        self.stdout.write(self.style.SUCCESS(f'  → {created} fake students created'))

    def create_fake_memberships(self, count):
        fake = Faker()
        students = list(Student.objects.all())
        orgs     = list(Organization.objects.all())
        created  = 0
        for _ in range(count * 3):
            if created >= count:
                break
            student = fake.random_element(students)
            org     = fake.random_element(orgs)
            if OrgMember.objects.filter(student=student, organization=org).exists():
                continue
            OrgMember.objects.create(
                student=student,
                organization=org,
                date_joined=fake.date_between(start_date="-3y", end_date="today"),
            )
            created += 1
        self.stdout.write(self.style.SUCCESS(f'  → {created} fake memberships created'))
