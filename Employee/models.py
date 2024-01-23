from django.db import models


class Dept(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, unique = True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25)
    dob = models.DateField()
    department = models.ForeignKey(Dept,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    title = models.CharField(max_length=50)
    agenda = models.TextField()
    # members = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(Employee)
    datentime = models.DateTimeField(auto_now_add=True)
    meeting_time = models.DateTimeField()
    is_finished = models.BooleanField()

    def __str__(self):
        return self.title