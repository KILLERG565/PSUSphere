#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsite.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

print("=== Sites Configuration ===")
sites = Site.objects.all()
if sites:
    for s in sites:
        print(f"✓ ID: {s.id}, Domain: {s.domain}, Name: {s.name}")
else:
    print("✗ No sites found!")

print("\n=== Social Apps Configuration ===")
apps = SocialApp.objects.all()
if apps:
    for app in apps:
        print(f"✓ Provider: {app.provider}, Name: {app.name}")
        print(f"  Sites: {', '.join([s.domain for s in app.sites.all()])}")
else:
    print("✗ No social apps configured. Follow instructions below to add them.\n")
    print("=" * 60)
    print("NEXT STEPS: Add Google OAuth (Optional)")
    print("=" * 60)
    print("""
1. Get Google OAuth Credentials:
   - Go to https://console.cloud.google.com/
   - Click "Select a Project" → "NEW PROJECT"
   - Name: "PSUSphere"
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth 2.0 Client ID"
   - Select "Web application"
   - Add Authorized redirect URIs:
     * http://127.0.0.1:8000/accounts/google/login/callback/
     * http://localhost:8000/accounts/google/login/callback/
   - Click "CREATE"
   - Copy the Client ID and Client Secret

2. Add to Django Admin:
   - Run: python manage.py createsuperuser (if not created)
   - Go to: http://127.0.0.1:8000/admin/
   - Login with your superuser credentials
   - Navigate to: Sites → localhost:8000
   - Change Domain name to: 127.0.0.1:8000
   - Change Display name to: PSUSphere (Local)
   - SAVE
   
3. Add Google Social App:
   - Go to: Social applications → Add Social application
   - Provider: Google
   - Name: Google OAuth
   - Client ID: (paste from step 1)
   - Secret key: (paste from step 1)
   - Sites: Select "127.0.0.1:8000"
   - SAVE

4. Test:
   - Visit http://127.0.0.1:8000/accounts/login/
   - You should see Google button now!
""")
