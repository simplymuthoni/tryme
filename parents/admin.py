from django.contrib import admin
from .models import (Parent)

models = [Parent]
for model in models:
    admin.site.register(model)