from django.db import models


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration_months = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    join_date = models.DateField()
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.PROTECT)
    membership_start = models.DateField()
    membership_end = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.phone})'

    @property
    def membership_status(self):
        from django.utils import timezone
        return 'Active' if self.active and self.membership_end >= timezone.localdate() else 'Expired'


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(blank=True, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['member', 'date'], name='one_checkin_per_member_per_day')]
        ordering = ['-date', '-check_in_time']

    def __str__(self):
        return f'{self.member.name} - {self.date}'
