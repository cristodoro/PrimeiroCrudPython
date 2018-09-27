from django.db import models

# Create your models here.
class Amigo(models.Model):
    nome = models . CharField(max_length = 200)
    data = models . DateTimeField('Data da amizade')

    def __str__(self):
        return self.nome

class Person(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    age = models.IntegerField()
    salary = models.FloatField(max_length= 100)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Pessoas'
