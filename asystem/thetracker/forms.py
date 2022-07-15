from django import forms
from django.forms import ModelForm
from .models import Job, Memo


# , Memo




# class CommunitiesSelectForm(forms.Form):
#     communities = forms.ModelMultipleChoiceField(queryset=Community.objects.all(),widget=forms.CheckboxSelectMultiple)



class JobSelectForm(forms.Form):
    jobs = forms.ModelMultipleChoiceField(queryset=Job.objects.all(),widget=forms.CheckboxSelectMultiple)


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'
