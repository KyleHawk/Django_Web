from django import forms
from myapp1.models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = {'item', 'client', 'num_of_items'}
        widgets = {'client': forms.RadioSelect}
        labels = {'num_of_items': 'Quantity', 'client': 'Client Name'}

class InterestForm(forms.Form):
    interested = forms.ChoiceField(choices=[(1,'Yes'),(2,'No')], widget=forms.RadioSelect)
    quantity = forms.IntegerField(min_value=1)
    comments = forms.CharField(label='Additional Comments', widget=forms.Textarea, required=False)
