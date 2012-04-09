from django.views.generic import FormView
from search.forms import SearchForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from bn.utils import bn
import simplejson as json
from django import http

class SearchView(FormView):
    template_name = 'index.html'
    form_class = SearchForm

    def post(self, request):
        if self.request.POST['fmt'] == 'json':
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                (flats, header) = bn.get_flats(form.cleaned_data)
                return http.HttpResponse(json.dumps((header, map(unicode,flats))),
                                         content_type='application/json')
                return super(SearchView, self).post(request)
        else:
            return super(SearchView, self).post(request)

    def form_valid(self, form):
        (flats, header) = bn.get_flats(form.cleaned_data)
        return self.render_to_response(self.get_context_data(form=form, flats=flats, header = header))
