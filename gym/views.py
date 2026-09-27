from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import AttendanceForm, MemberForm, MembershipPlanForm
from .models import Attendance, Member, MembershipPlan


def dashboard(request):
    today = timezone.localdate()
    active = Member.objects.filter(active=True, membership_end__gte=today)
    return render(request, 'gym/dashboard.html', {
        'total_members': Member.objects.count(), 'active_members': active.count(),
        'expired_members': Member.objects.exclude(pk__in=active).count(),
        'today_checkins': Attendance.objects.filter(date=today).count(),
        'recent_members': Member.objects.select_related('membership_plan').order_by('-join_date')[:5],
        'today_attendance': Attendance.objects.select_related('member').filter(date=today),
        'plans': MembershipPlan.objects.all(),
    })


def member_list(request):
    query = request.GET.get('q', '')
    members = Member.objects.select_related('membership_plan').all()
    if query:
        members = members.filter(Q(name__icontains=query) | Q(phone__icontains=query))
    return render(request, 'gym/members.html', {'members': members, 'query': query})


def save_form(request, form_class, instance, template, title, success, redirect_name):
    form = form_class(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save(); messages.success(request, success); return redirect(redirect_name)
    return render(request, template, {'form': form, 'title': title})


def member_create(request): return save_form(request, MemberForm, None, 'gym/form.html', 'Add Member', 'Member added successfully.', 'member_list')
def member_update(request, pk): return save_form(request, MemberForm, get_object_or_404(Member, pk=pk), 'gym/form.html', 'Edit Member', 'Member updated successfully.', 'member_list')

def member_delete(request, pk):
    obj = get_object_or_404(Member, pk=pk)
    if request.method == 'POST': obj.delete(); messages.success(request, 'Member deleted successfully.'); return redirect('member_list')
    return render(request, 'gym/confirm_delete.html', {'object': obj, 'cancel_url': 'member_list'})

def plan_list(request): return render(request, 'gym/plans.html', {'plans': MembershipPlan.objects.all()})
def plan_create(request): return save_form(request, MembershipPlanForm, None, 'gym/form.html', 'Add Membership Plan', 'Plan added successfully.', 'plan_list')
def plan_update(request, pk): return save_form(request, MembershipPlanForm, get_object_or_404(MembershipPlan, pk=pk), 'gym/form.html', 'Edit Membership Plan', 'Plan updated successfully.', 'plan_list')

def plan_delete(request, pk):
    obj = get_object_or_404(MembershipPlan, pk=pk)
    if request.method == 'POST': obj.delete(); messages.success(request, 'Plan deleted successfully.'); return redirect('plan_list')
    return render(request, 'gym/confirm_delete.html', {'object': obj, 'cancel_url': 'plan_list'})

def attendance_list(request): return render(request, 'gym/attendance.html', {'records': Attendance.objects.select_related('member')})
def attendance_create(request): return save_form(request, AttendanceForm, None, 'gym/form.html', 'Record Check-in', 'Check-in recorded successfully.', 'attendance_list')
def attendance_update(request, pk): return save_form(request, AttendanceForm, get_object_or_404(Attendance, pk=pk), 'gym/form.html', 'Edit Attendance / Check-out', 'Attendance updated successfully.', 'attendance_list')

def attendance_delete(request, pk):
    obj = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST': obj.delete(); messages.success(request, 'Attendance record deleted successfully.'); return redirect('attendance_list')
    return render(request, 'gym/confirm_delete.html', {'object': obj, 'cancel_url': 'attendance_list'})
