from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    ongoing = models.BooleanField(default=True)
    quick_description = models.CharField(max_length=140)
    full_description = models.TextField()

    def __str__(self):
        return self.name


class GeneralSubsystem(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=8)
    short_description = models.CharField(max_length=150)
    full_description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subsystem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    general_subsystem = models.ForeignKey(GeneralSubsystem, on_delete=models.CASCADE)
    quick_update = models.CharField(max_length=140)
    MEETING_FREQUENCY_CHOICES = (
        ('Weekly', 'Every week'),
        ('Biweekly', 'Every other week'),
        ('Monthly', 'Once a month'),
    )
    meeting_frequency = models.CharField(max_length=20, choices=MEETING_FREQUENCY_CHOICES, default='Weekly')
    DAYS = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    meeting_day = models.CharField(max_length=20, choices=DAYS, default='Monday')
    meeting_time = models.TimeField(default=timezone.now)
    meeting_location = models.CharField(max_length=50, default='Toomey 140')
    lead_name = models.CharField(max_length=200)
    lead_email = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s (%s)' % (self.general_subsystem, self.project)


class Timeline(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # MONTHS = (
    #     ('January', 'January'),
    #     ('February', 'February'),
    #     ('March', 'March'),
    #     ('April', 'April'),
    #     ('May', 'May'),
    #     ('June', 'June'),
    #     ('July', 'July'),
    #     ('August', 'August'),
    #     ('September', 'September'),
    #     ('October', 'October'),
    #     ('November', 'November'),
    #     ('December', 'December'),
    # )
    # month = models.CharField(max_length=200, choices=MONTHS, default='January')
    # year = models.IntegerField(default=2016)
    text = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s (%s)' % (self.date, self.project)
