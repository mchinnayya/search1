from django import forms
from contact.models import Branch, Contact


class EmergencyDetailsForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'style': "width: 100%"}), label="Branch", required=True)
    contact_name = forms.CharField(max_length=255, label="Area Name", required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    extension_number = forms.IntegerField(label="Extension No.", required=True,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=255, label="Name", required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}), label="Email Address", required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Image", required=False)

    class Meta:
        model = Contact
        fields = ('branch', 'contact_name', 'extension_number', 'name', 'email', 'image',)


