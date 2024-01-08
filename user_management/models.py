from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', _('Male')
        FEMALE = 'FEMALE', _('Female')
        OTHERS = 'OTHERS', _('Others')
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, null=True, blank=True, choices=Gender.choices)
    geolocation = models.CharField(max_length=255, null=True, blank=True,)
    company = models.ForeignKey(to="organization.Company", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class EmployeeHistory(models.Model):
    class EMPLOYEE_EVENT_CHOICES(models.TextChoices):
        RESIGNATION = 'RESIGNATION', _('Resignation')
        TERMINATION = 'TERMINATION', _('Termination')
        REJOINING = 'REJOINING', _('Rejoining')
        OTHER = 'OTHER', _('Other')
    
    user = models.ForeignKey(to='user_management.UserProfile', on_delete=models.CASCADE)
    event_date = models.DateField(null=True, blank=True)
    event_type = models.CharField(max_length=255, choices=EMPLOYEE_EVENT_CHOICES.choices, null=True, blank=True)
    note = models.TextField( blank=True, null=True)
    last_working_date = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username
    
    class Meta:
        ordering = ['-id']