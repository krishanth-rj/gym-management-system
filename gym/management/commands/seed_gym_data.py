from datetime import time, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from gym.models import Attendance, Member, MembershipPlan


class Command(BaseCommand):
    help = 'Creates simple sample gym plans, members, and attendance.'

    def handle(self, *args, **options):
        basic, _ = MembershipPlan.objects.get_or_create(name='Basic', defaults={'duration_months': 1, 'price': 799, 'description': 'Access to gym equipment.'})
        standard, _ = MembershipPlan.objects.get_or_create(name='Standard', defaults={'duration_months': 3, 'price': 1999, 'description': 'Gym access and trainer guidance.'})
        premium, _ = MembershipPlan.objects.get_or_create(name='Premium', defaults={'duration_months': 12, 'price': 6999, 'description': 'Complete fitness membership.'})
        today = timezone.localdate()
        entries = [('Rahul Sharma', '9876543210', 'rahul@example.com', 23, 'Male', basic, today + timedelta(days=25)), ('Vishal Kumar', '9876543211', 'vishal@example.com', 27, 'Male', standard, today + timedelta(days=70)), ('Vimal Raj', '9876543212', 'vimal@example.com', 25, 'Male', premium, today + timedelta(days=300)), ('Arjun Nair', '9876543213', 'arjun@example.com', 29, 'Male', basic, today - timedelta(days=4))]
        for name, phone, email, age, gender, plan, end in entries:
            member, _ = Member.objects.get_or_create(phone=phone, defaults={'name': name, 'email': email, 'age': age, 'gender': gender, 'join_date': today - timedelta(days=15), 'membership_plan': plan, 'membership_start': today - timedelta(days=15), 'membership_end': end, 'active': True})
            if end >= today: Attendance.objects.get_or_create(member=member, date=today, defaults={'check_in_time': time(7, 30)})
        self.stdout.write(self.style.SUCCESS('Sample gym data is ready.'))
