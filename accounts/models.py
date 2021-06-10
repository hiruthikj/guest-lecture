from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# YEAR_OF_STUDY_CHOICES = [ (i,i) for i in range(1,5) ]

class CustomUser(AbstractUser):
    class UserTypes(models.TextChoices):
        STUDENT = 'STUD', _("Student")
        FACULTY = 'FCLT', _("Faculty")
        CIR_FACULTY = 'CIR', _("CIR Faculty")
        GUEST = 'GUEST', _("Guest Lecturer")
        OTHERS = 'OTHER', _("External Students")
    
    user_type = models.CharField(_("User Type"), max_length=10, choices=UserTypes.choices, default=UserTypes.OTHERS)
    phone_no = models.CharField(_("Phone Number"), max_length=10, unique=True, help_text='10-digit phone number',null=True, blank=True)

    def __str__(self):
        return f"{self.username}"

    def get_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.get_username()

    def get_username(self):   
        return self.username

    # def get_absolute_url(self):
    #     return reverse('lecture_app:home', kwargs={'username': self.get_username()})

    # class Meta:
    #     ordering = ['dept_fk__dept_name']