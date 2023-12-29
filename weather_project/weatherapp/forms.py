from django.forms import ModelForm, TextInput
from .models import Cities

class CityForm(ModelForm):
    class Meta:
        model = Cities
        fields = ['city']
        widgets = {
            'city': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder