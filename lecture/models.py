from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.shortcuts import redirect
from django.core.validators import MinValueValidator, MaxValueValidator

# STATUSES = [
#     (1, 'On-Schedule'),
#     (2, 'Completed'),
#     (3, 'Cancelled'),
#     (4, 'Tentatitve'),
# ]

User = get_user_model()


class Department(models.Model):
    dept_code = models.CharField(_("Department Code"), max_length=10, unique=True)
    dept_name = models.CharField(_("Department Name"), max_length=50)

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    # class YearOfStudyChoices(models.IntegerChoices):
    #     YEAR1 = 1,1
    #     YEAR2 = 2,2
    #     YEAR3 = 3,3
    #     YEAR4 = 4,4

    account = models.OneToOneField(User, verbose_name=_("Account"), on_delete=models.CASCADE)
    reg_no = models.CharField(_("Registration Number"), max_length=50, null=True, blank=True, unique=True)
    # year_of_study = models.PositiveIntegerField(_("Year of Study"), null=True, blank=True, choices=YearOfStudyChoices.choices) 
    dept_fk = models.ForeignKey('Department', verbose_name=_("Department"), on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.account.get_username()}"

    def get_name(self):
        return f"{self.account.get_name()}"


class Faculty(models.Model):
    account = models.OneToOneField(User, verbose_name=_("Account"), on_delete=models.CASCADE)
    # emp_no = models.CharField(_("Employee Number"), max_length=50, null=True, blank=True, unique=True)
    dept_fk = models.ForeignKey('Department', verbose_name=_("Department"), on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.account.get_username()}"

    def get_name(self):
        return f"{self.account.get_name()}"


class CIRFaculty(models.Model):
    account = models.OneToOneField(User, verbose_name=_("Account"), on_delete=models.CASCADE)
    # emp_no = models.CharField(_("Employee Number"), max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.account.get_username()}"

    def get_name(self):
        return f"{self.account.get_name()}"


class ExternalUser(models.Model):
    account = models.OneToOneField(User, verbose_name=_("Account"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account.get_username()}"

    def get_name(self):
        return f"{self.account.get_name()}"


class Event(models.Model):
    class EventStatus(models.TextChoices):
        ON_SCHEDULE = 'ON', _("On-Schedule")
        COMPLETED = 'COMP', _("Completed")
        CANCELLED = 'X', _("Cancelled")
        TENTATIVE = 'TNTV', _("Tentative")

    class EventType(models.TextChoices):
        CIR = 'CIR', _("CIR")
        DEPT = 'DEPT', _("Department")
        OTHER = 'OTHER', _("Other")
    #e_id = models.AutoField(primary_key=True)
    event_name = models.CharField(_("Event Name"), max_length=200)
    start_date = models.DateTimeField(_("Start Date"), null=True, blank=True,auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(_("End Date"), null=True, blank=True, auto_now=False, auto_now_add=False)
    max_seats = models.PositiveIntegerField(_("Maximum Seats"), null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])

    description = models.CharField(_("Descrtiption"), max_length=100, default="No description")
    summary = models.TextField(_("Summary"), null=True, blank=True)
    place = models.CharField(_("Location"), max_length=200)
    status = models.CharField(_("Status"), choices=EventStatus.choices, default=EventStatus.ON_SCHEDULE, max_length=20)
    type = models.CharField(_("Type"), choices=EventType.choices, default=EventType.CIR, max_length=20)
    created_by = models.ForeignKey('accounts.CustomUser', verbose_name=_("Created by"), on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return f"{self.event_name}"

    def get_absolute_url(self):
        return reverse("lecture_app:event", kwargs={"pk": self.pk})

    def register_to_event(self, user):
        applications.objects.create(
            student = user,
            event = self,
            # time_registered = timezone.now()
        )

    def remove_registration_from_event(self, user):
        existing_application = applications.objects.get(student=user, event=self)
        existing_application.delete()
      
    
class applications(models.Model):
    student = models.ForeignKey('accounts.CustomUser',verbose_name='student',on_delete=models.CASCADE)
    event = models.ForeignKey('Event',verbose_name='Event',on_delete=models.CASCADE)
    time_registered = models.DateTimeField(_("Time Registered"), auto_now_add=True, null=True, blank=True)

    def has_applied(self, user_pk, event_pk):
        try:
            applications.objects.get(student=user_pk, event=event_pk)
            return True
        except:
            return False

    
    def __str__(self):
        return f"{self.event} - {self.student}"

    