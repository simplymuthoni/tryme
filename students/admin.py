from django.contrib import admin
from .models import (Student)

models = [Student]
for model in models:
    admin.site.register(model)