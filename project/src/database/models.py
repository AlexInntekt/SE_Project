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