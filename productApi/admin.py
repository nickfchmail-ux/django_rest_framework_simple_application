from django.contrib import admin
from .models import UserDetail, UserProfile  # Relative import from the same app

admin.site.register(UserDetail)
admin.site.register(UserProfile)
