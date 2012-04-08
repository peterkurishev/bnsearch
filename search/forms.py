from django.forms import ModelForm, CheckboxSelectMultiple
from search.models import SearchCache

class SearchForm(ModelForm):
    class Meta:
        model = SearchCache
        widgets = {'metro_stations': CheckboxSelectMultiple}
