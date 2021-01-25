from django.db import models

# Create your models here.


class LanguageStream(models.Model):
    name = models.CharField(max_length=50)
    abrv = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(LanguageStream, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} {}".format(self.name, self.language.abrv)

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    abrv = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Faculties'

class Department(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.ManyToManyField(Subject)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        try:
            department_name = self.department.name
        except AttributeError:
            department_name = "No department assigned"

        return "{} {} ({})".format(self.name, self.surname, department_name)


class TeachingHour(models.Model):
    DAY = [
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday')
    ]

    TYPE = [
        ('Course','Course'),
        ('Laboratory','Laboratory'),
        ('Seminary','Seminary'),
        ('Activity','Activity'),
    ]

    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    subject   = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    day       = models.CharField(null=True, max_length=20, choices=DAY, default='Monday')
    time      = models.TimeField(null=True)
    hours     = models.IntegerField(null=True, default=2)
    ttype     = models.CharField(null=True, max_length=20, choices=TYPE, default='Course')

    def __str__(self):
        return "{} - {} {} {} {}".format(self.subject.name, self.professor.name, self.professor.surname, self.day, self.time)