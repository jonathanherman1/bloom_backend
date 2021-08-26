from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Company(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=150, blank=True)
  url = models.URLField(blank=True)
  summary = models.CharField(max_length=100, blank=True)
  interested = models.BooleanField(default=False, null=True)
  glassdoor_rating = models.DecimalField(max_digits=5, decimal_places=1)
  PUBLIC = 'Public'
  PRIVATE = 'Private'
  NON_PROFIT = 'Non_Profit'
  business_structure = [(PUBLIC, 'Public'), (PRIVATE, 'Private'), (NON_PROFIT, 'Non_Profit')]
  business_structure = models.CharField(
    max_length=20,
    choices=business_structure,
    default='Public', 
    blank=True
  )
  notes = models.TextField(max_length=300, blank=True)
  archived = models.BooleanField(default=False, null=True)
  def __str__(self):
    return self.name

class Contact(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=100)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") 
  phone = models.CharField(validators=[phone_regex], max_length=16, blank=True)
  email = models.EmailField(max_length=200, blank=True)
  department = models.CharField(max_length=100, blank=True)
  first_contact_through = models.CharField(max_length=100, blank=True)
  notes = models.TextField(max_length=300, blank=True)
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
  def __str__(self):
    return self.name

class Opportunity(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=100)
  date = models.DateField()
  notes = models.CharField(max_length=300, blank=True)
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  rating_choices = [(ONE, 1), (TWO, 2), (THREE, 3), (FOUR, 4), (FIVE, 5)]
  rating = models.CharField(
    max_length=2,
    choices=rating_choices,
    default=3, 
    blank=True
  )
  location = models.CharField(max_length=150, blank=True)
  pros = models.TextField(blank=True)
  cons = models.TextField(blank=True)
  salary = models.CharField(max_length=100, blank=True)
  responsibilities = models.TextField(blank=True)
  requirements = models.TextField(blank=True)
  
  STARTED = 'started'
  READ_JOB_DESCRIPTION = 'read_job_description'
  DETERMINED_IF_QUALIFIED = 'determined_if_qualified'
  RESEARCHED_COMPANY = 'researched_company'
  OPTIMIZED_RESUME = 'optimized_resume_for_role'
  IN_CONTACT = 'in_contact'
  APPLIED = 'applied'
  INTERVIEWED = 'interviewed'
  NEGOTIATED = 'negotiated'
  ACCEPTED_OFFER = 'accepted_offer'
  PASS = 'decided_to_pass'
  NO_OFFER_EXTENDED = 'no_offer_extended'
  status_choices = [
    (STARTED, 'Started'), 
    (READ_JOB_DESCRIPTION, 'Read Job Description'), 
    (RESEARCHED_COMPANY,'Researched Company'), 
    (OPTIMIZED_RESUME,'Optimized Resume'), 
    (IN_CONTACT,'In Contact'), 
    (APPLIED,'Applied'), 
    (INTERVIEWED,'Interviewed'), 
    (NEGOTIATED,'Negotiated'), 
    (ACCEPTED_OFFER,'Accepted Offer'), 
    (PASS,'Decided to Pass'), 
    (NO_OFFER_EXTENDED,'No Offer Extended')
  ]
  status = models.CharField(
    max_length=100, 
    choices=status_choices,
    default=STARTED,
    blank=True
  )
  years_experience_required = models.CharField(max_length=100, blank=True)
  role_list_url = models.URLField(max_length=100, blank=True)
  listing_source = models.CharField(max_length=100, blank=True)
  keywords = models.CharField(max_length=100, blank=True)
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
  contacts = models.ManyToManyField(Contact, blank=True)
  def __str__(self):
    return self.name

class Activity(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=100)
  date = models.DateField()
  type = models.CharField(max_length=50, blank=True)
  contact_method = models.CharField(max_length=100, blank=True, null=True)
  notes = models.TextField(max_length=300, blank=True, null=True)
  contacts = models.ManyToManyField(Contact, blank=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
  opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self):
    return self.name
