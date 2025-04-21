from django import forms
from .models import Book


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
