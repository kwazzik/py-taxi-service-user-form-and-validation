import re

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Driver, Car


class DriverCreationForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", )


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise forms.ValidationError(
                "The license number must be 8 characters long."
            )

        pattern = r"^[A-Z]{3}\d{5}$"
        if not re.match(pattern, license_number):
            raise forms.ValidationError(
                "The license format is incorrect. "
                "It should be: 3 uppercase letters and 5 "
                "numbers (for example, ABC12345)."
            )

        return license_number


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }
