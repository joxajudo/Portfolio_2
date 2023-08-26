from django.forms import ModelForm

from app.models import Contact


class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
