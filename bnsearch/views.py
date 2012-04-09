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
        form_id = form.save()
        print form_id
        (flats, header) = bn.get_flats(form.cleaned_data)
        # for flat in flats:
        #     ss = ""
        #     for field in flat._meta.fields:
        #         try:
        #             print "%s: %s" % (field.name, getattr(flat, field.name))
        #         except:
        #             print "Field %s does not exist in this model" % (field.name,)
        #             continue
        
        return self.render_to_response(self.get_context_data(form=form, flats=flats, header=header))

class GetMetroStationsMixin():
    pass

