from django.views.generic import FormView
from search.forms import SearchForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from bn.utils import bn

class SearchView(FormView):
    template_name = 'index.html'
    form_class = SearchForm

    def form_valid(self, form):
        super(SearchView, self).form_valid(form)
        form.save()
        flats = bn.get_flats(form.cleaned_data)
        return self.render_to_response(self.get_context_data(form=form, flats=flats))

class GetMetroStationsMixin():
    pass

