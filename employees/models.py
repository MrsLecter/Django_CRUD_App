from django.db import models

class Deparment(models.Model):
    name = models.TextField(null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.TextField(null=False)
    surname = models.TextField(null=False)
    age = models.IntegerField(default=18, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    department = models.ForeignKey(Deparment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)
