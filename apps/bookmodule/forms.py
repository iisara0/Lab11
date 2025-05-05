from django import forms
from .models import Book, Students, Students2,StudentImage



class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'age', 'address', ]
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'address': 'City',
        }


class Student2Form(forms.ModelForm):
    class Meta:
        model = Students2
        fields = '__all__'

class StudentImageForm(forms.ModelForm):
    class Meta:
        model = StudentImage
        fields = '__all__'


    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance











class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter book title',
            'class': 'mycssclass',
            'id': 'jsID'
        })
    )

    author = forms.CharField(
        max_length=50,
        required=True,
        label="Author"
    )

    price = forms.DecimalField(
        required=True,
        label="Price",
        min_value=0,
        initial=0.0
    )
    edition = forms.IntegerField(
        required=True,
        label="Edition",
        min_value=1,
        initial=1,
        widget=forms.NumberInput()
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']




