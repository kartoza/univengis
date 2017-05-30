# coding=utf-8
from django import forms
from .models import DataTable, SlotData


class DataTableForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    document = forms.FileField(
        label='Select a CSV file to import:',
        required=False
    )

    class Meta:
        model = DataTable
        fields = ('title', 'document',)

    def __init__(self, *args, **kwargs):
        super(DataTableForm, self).__init__(*args, **kwargs)

    def save(self):
        instance = super(DataTableForm, self).save(commit=False)
        instance.save()
        return instance
