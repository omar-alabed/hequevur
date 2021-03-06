from .validators import validate_file_extension
from .generics import IntegerRangeField
from django.db import models


class Department(models.Model):
    department_name = models.TextField()

    def __str__(self):
        return self.department_name


class Candidate(models.Model):
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    years_of_experience = IntegerRangeField(min_value=0, max_value=30, default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='files/%Y/%m/%d/', validators=[validate_file_extension],
                              max_length=255, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
