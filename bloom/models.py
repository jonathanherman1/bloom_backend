from django.db import models

class Contacts(models.Model):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=30)
  email = models.CharField(max_length=50)
  department = models.CharField(max_length=100)
  first_contact_through = models.CharField(max_length=100)
  notes = models.TextField()
  # opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
  # company = models.ForeignKey(Company, on_delete=models.CASCADE)
  # activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  
class Activity(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField()
  type = models.CharField(max_length=50)
  # contacts = models.ManyToManyField(Contacts)
  contact_method = models.CharField(max_length=100)
  # opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
  # company = models.ForeignKey(Company, on_delete=models.CASCADE)
  notes = models.TextField()

  def __str__(self):
    return self.name

class Opportunity(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField()
  # activities = models.ForeignKey(Activity, on_delete=models.CASCADE)
  # company = models.OneToOneField(Company, on_delete=models.CASCADE)
  # contacts = models.ManyToManyField(Contacts)
  # interest_choices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
  # interest = models.CharField(
  #   max_length=2,
  #   choices=interest_choices,
  #   default=3
  # )
  # location = models.CharField(max_length=100)
  # pros = models.CharField(max_length=100)
  # cons = models.CharField(max_length=100)
  # salary = models.CharField(max_length=100)
  # responsibilities = models.CharField(max_length=100)
  # requirements = models.CharField(max_length=100)
  # five_steps = models.CharField(max_length=100)
  # status = models.CharField(max_length=100)
  # years_experience_required = models.CharField(max_length=100)
  # role_list_url = models.CharField(max_length=100)
  # listing_source = models.CharField(max_length=100)
  notes = models.CharField(max_length=100)
  # latest_activity = models.CharField(max_length=100)
  # keywords = models.CharField(max_length=100)

  
