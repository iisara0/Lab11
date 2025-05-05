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


#Task 1 LAB11
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



class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Students2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)
    image = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.name


class StudentImage(models.Model):
    student = models.OneToOneField(Students2, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_photo/')

    def __str__(self):
        return self.student.name





