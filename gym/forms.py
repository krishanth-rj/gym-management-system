from django import forms
from .models import Attendance, Member, MembershipPlan


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MemberForm(StyledModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'join_date': forms.DateInput(attrs={'type': 'date'}),
            'membership_start': forms.DateInput(attrs={'type': 'date'}),
            'membership_end': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(), 'age': forms.NumberInput(),
        }

    def clean(self):
        data = super().clean()
        if data.get('membership_start') and data.get('membership_end') and data['membership_end'] < data['membership_start']:
            self.add_error('membership_end', 'End date cannot be before start date.')
        return data


class MembershipPlanForm(StyledModelForm):
    class Meta:
        model = MembershipPlan
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows': 3}), 'duration_months': forms.NumberInput(), 'price': forms.NumberInput(attrs={'step': '0.01'})}


class AttendanceForm(StyledModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}), 'check_in_time': forms.TimeInput(attrs={'type': 'time'}), 'check_out_time': forms.TimeInput(attrs={'type': 'time'})}

    def clean(self):
        data = super().clean()
        if data.get('check_in_time') and data.get('check_out_time') and data['check_out_time'] < data['check_in_time']:
            self.add_error('check_out_time', 'Check-out cannot be before check-in.')
        return data
