from django.db import models



class Card(models.Model):
    card_number = models.IntegerField()


class Department(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    card = models.OneToOneField( Card, on_delete=models.PROTECT)
    department = models.ForeignKey( Department, on_delete=models.CASCADE ,  related_name='student')
    courses = models.ManyToManyField(Course , related_name='student')


class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

    def __str__(self):
        return self.title



class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city



class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


