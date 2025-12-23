from django.db import models

class StudentForm(models.Model):
    Sname = models.CharField(max_length=50)
    Sage = models.IntegerField()
    Semail = models.EmailField()

    def __str__(self):
        return self.Sname