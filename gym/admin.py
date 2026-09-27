from django.contrib import admin
from .models import Attendance, Member, MembershipPlan


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'membership_plan', 'membership_end', 'active')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('active', 'gender', 'membership_plan')


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_months', 'price')
    search_fields = ('name',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'check_in_time', 'check_out_time')
    search_fields = ('member__name',)
    list_filter = ('date',)
