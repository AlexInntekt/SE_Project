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


class Professor(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	subject = models.ManyToManyField(Subject)

	def __str__(self):
		return self.name