from django.db import models

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