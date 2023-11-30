from django import forms


class ItemForm(forms.Form):
    item_text = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'placeholder': 'Enter a TODO item',
            'class': 'form-control input-lg',
        })
    )
