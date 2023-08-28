from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from choices.role_types import USER_ROLES
from choices.lead_src import LEAD_SOURCE
from choices.lead_status import LEAD_STATUS
from choices.agent_type import AGENT_TYPE


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, phone, role, title, dob,address, createdOn  , password=None):
        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(email=self.normalize_email(email), name=name, phone=phone, role=role, title = title, dob = dob, address=address, createdOn = createdOn)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, role, title, dob,address, createdOn , password=None):
        if is_superadmin.get('is_superadmin') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, phone, role, password, title, dob,address, createdOn )
class UserProfile(AbstractBaseUser):
    title = models.CharField("Title", max_length=50, blank=True, null=True)
    name = models.CharField("Name", max_length=255)
    email = models.EmailField("E-mail", blank=True, null=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField("Date of Birth", blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=  USER_ROLES)
    # createdBy = models.ForeignKey(User, related_name='c ontact_created_by', on_delete=models.CASCADE)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)

    # user_permissions = models.ManyToManyField(RolePermissions, on_delete = models.CASCADE)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'role', 'address']
    def __str__(self):
        return self.name


class Superadmin(UserProfile):
    is_superadmin = models.BooleanField(default=True)

class Admin(UserProfile):
    is_admin = models.BooleanField(default=True)


class Agent(UserProfile):
    is_staff = models.BooleanField("Staff",default=False)
    agent_type = models.CharField("Agent Type", max_length=255,blank=True, null=True, choices= AGENT_TYPE)
    def __str__(self):
        return self.name

class CustomerCare(UserProfile):
    # is_staff = models.BooleanField("Staff", default=False)
    is_customer_care = models.BooleanField("Customer Care", default=True)
    department = models.CharField(max_length=100)


class Customer(UserProfile):
    status = models.CharField("Status of Lead", max_length=255,blank=True, null=True, choices= LEAD_STATUS)
    source = models.CharField("Source of Lead", max_length=255,blank=True, null=True, choices=LEAD_SOURCE)
    isActive = models.BooleanField("Active",default=False)
    dnc = models.BooleanField("Do Not Call", default= False)
    description = models.TextField(blank=True, null=True)
#     # assigned_to = models.ManyToManyField(User, related_name='lead_assigned_users')
#
    def __str__(self):
        return self.name


# class Escalators(Userprofile):
# class TeamManager(Userprofile):
# class TeamLead(Userprofile):
#