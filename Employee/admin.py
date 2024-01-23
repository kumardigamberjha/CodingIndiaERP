from django.contrib import admin

from Employee.models import Dept, Employee, Meeting


admin.site.register(Dept)
admin.site.register(Employee)
admin.site.register(Meeting)