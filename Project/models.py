from django.db import models

class ProjectCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    subcat = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectModel(models.Model):
    name = models.CharField(max_length=100)
    projectdate = models.DateField(auto_now_add=True)
    cat = models.ForeignKey(ProjectCategoryModel, on_delete=models.CASCADE)
    desc = models.TextField(default="")
    img = models.ImageField(blank=True, null=True)
    finishdatetime = models.DateTimeField()
    payment = models.IntegerField()
    paymentReceived = models.FloatField()


    # file = models.FileField()
    # Email


    def __str__(self):
        return self.name
