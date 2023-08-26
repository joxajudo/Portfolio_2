from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite, ModelAdmin
from django.forms import ModelForm

from app.forms import ContactModelForm
from app.models import Contact


# admin.site.register(Contact)

class ContactAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"


product_admin_site = ContactAdminSite(name='contact_admin')
product_admin_site.register(Contact)


# --------------------------------------------------------------------

class ContactModelForm1(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactModelForm1, self).__init__(*args, **kwargs)
        self.fields['name'].help_text = 'Contact name'
        self.fields['email'].help_text = 'Contact email'
        self.fields['subject'].help_text = 'Contact subject'
        self.fields['text'].help_text = 'Contact text'

    class Meta:
        model = Contact
        exclude = ()


# --------------------------------------------------------------------

MAX_OBJECTS = 4


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    form = ContactModelForm
    list_display = ('name', 'email', 'subject', 'text')  # table kurinishida chiqarish
    list_per_page = 8  # pagenation qilish
    search_fields = ('name',)  # search qilish
    ordering = ('name',)  # order by

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)
