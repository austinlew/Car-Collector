from django.db import models

TIME = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

# Create your models here.
class Upgrade(models.Model):
  item = models.CharField(max_length=50)
  brand = models.CharField(max_length=20)

def __str__(self):
  return self.item


class Car(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.TextField(max_length=100)
  upgrades = models.ManyToManyField(Upgrade)

def __str__(self):
  return f'{self.brand} ({self.id})'


class Show(models.Model):
  date = models.DateField('Show Date')
  time = models.CharField(
    max_length=1,
    choices=TIME,
    default=TIME[0][0]
  )
  car = models.ForeignKey(
    Car,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']