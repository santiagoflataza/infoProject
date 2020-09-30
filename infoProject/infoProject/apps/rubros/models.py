from django.db import models

class Rubro(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.TextField(null = False)
