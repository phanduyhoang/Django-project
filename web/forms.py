from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'email', 'phone_number', 'comment']
        
    def __init__(self, *args, **kwargs):
        super(InfoForm, self).__init__(*args, **kwargs)
        # Add custom styling to each form field
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': f'custom-{field_name}'})