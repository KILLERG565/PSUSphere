#!/usr/bin/env python
"""
Setup script to configure PSUSphere for local development
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsite.settings')
django.setup()

from django.contrib.sites.models import Site
from django.contrib.auth.models import User

print("=" * 60)
print("PSUSphere Local Setup")
print("=" * 60)

# 1. Update Site
print("\n[1] Updating Site Configuration...")
site = Site.objects.get_or_create(id=1)[0]
site.domain = '127.0.0.1:8000'
site.name = 'PSUSphere (Local)'
site.save()
print(f"✓ Site updated: {site.domain} - {site.name}")

# 2. Create superuser if needed
print("\n[2] Checking Superuser...")
if User.objects.filter(is_superuser=True).exists():
    admin = User.objects.filter(is_superuser=True).first()
    print(f"✓ Superuser exists: {admin.username}")
else:
    print("✗ No superuser found!")
    print("\nCreate a superuser by running:")
    print("  python manage.py createsuperuser")

print("\n" + "=" * 60)
print("QUICK START - Google OAuth Setup (Optional)")
print("=" * 60)
print("""
1. Create superuser (if not done):
   python manage.py createsuperuser

2. Run development server:
   python manage.py runserver

3. Go to Django Admin:
   http://127.0.0.1:8000/admin/

4. Create Google OAuth App:
   a) Get credentials from: https://console.cloud.google.com/
   b) Add Social Application in Admin
   c) Fill in Client ID and Secret

5. Test Social Login:
   http://127.0.0.1:8000/accounts/login/
""")
print("=" * 60)
