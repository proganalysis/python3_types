from django.contrib import admin
from django import forms
from .models import ModuleStorage
import json


class ModuleStorageModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModuleStorageModelForm, self).__init__(*args, **kwargs)
        self.initial['modules'] = self.display_as_lines(self.instance.modules)

    def display_as_lines(self, value):
        data = json.loads(value)
        return "\n".join(data)


class ModuleStorageAdmin(admin.ModelAdmin):
    form = ModuleStorageModelForm

    def save_model(self, request, obj, form, change):
        data = obj.modules.split("\n")
        obj.modules = json.dumps(data)

        super(ModuleStorageAdmin, self).save_model(request, obj, form, change)

admin.site.register(ModuleStorage, ModuleStorageAdmin)