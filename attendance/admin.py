from django.contrib import admin
from .models import (Attendance)

models = [Attendance]
for model in models:
    admin.site.register(model)