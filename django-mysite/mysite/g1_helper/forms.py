from django import forms
from .models import G1File


class G1ParseGCIForm(forms.Form):
    """
    For parsing GCI strings
    """
    file_fields = ()

    gci_string = forms.CharField(
        max_length=255,
        label='Enter a GCI String',
        disabled=False,
        required=True,
        widget=forms.TextInput(attrs={'size': '150'})
    )

    file_name = forms.ModelChoiceField(
        label="Filename",
        queryset=G1File.objects.all()
    )












