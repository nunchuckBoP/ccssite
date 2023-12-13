from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job
from djmoney.models.fields import MoneyField
from ccsproject.settings import DEFAULT_MILEAGE_RATE
import datetime

# Create your models here.
class Timecodes(models.Model):
    number = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.number + ": " + self.description

class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateField(verbose_name="Start Date", null=False, blank=False)
    end_date = models.DateField(verbose_name="End Date", null=False, blank=False)
    submitted = models.DateTimeField(verbose_name="Submitted", null=True, blank=True)

    @property
    def is_submitted(self):
        if self.submitted is not null:
            return True
        else:
            return False
        # end if

    def __str__(self):
        return "timesheet_" + self.start_date

class TimeEntry(models.Model):
    sheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(blank=False, null=False)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, null=True, blank=True)
    code = models.ForeignKey(Timecodes, on_delete=models.DO_NOTHING, null=False, blank=False)
    hours = models.FloatField(default=0.0, null=False, blank=False)

    def __str__(self):
        return self.date + ", " + self.job + ", " + self.code + ", " + self.hours

class Expense(models.Model):
    sheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(blank=False, null=False)
    job = models.ForeignKey(Job, verbose_name="Job", on_delete=models.PROTECT, null=True, blank=True)
    miles = models.FloatField(verbose_name="Miles", default=0, null=False, blank=False)
    mileage_rate = MoneyField(verbose_name="Mileage Rate", max_digits=3, decimal_places=2, default=DEFAULT_MILEAGE_RATE, default_currency="USD")
    air_fare = MoneyField(verbose_name="Air Fare", max_digits=7, decimal_places=2, default=0.0, default_currency="USD")
    hotel = MoneyField(verbose_name="Hotel", max_digits=5, decimal_places=2, default=0.0, blank=False, null=False, default_currency="USD")
    explanation = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "expense " + self.date + ", " + self.amount + ", " + self.explanation