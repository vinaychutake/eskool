from django.shortcuts import render
from django.views.generic import View
from academics_management.forms import AcademicsForm
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from academics_management.api import year_api
import pdb
from django.contrib.humanize.templatetags.humanize import naturaltime

# Create your views here.
class AcademicsYearView(View):
    """
    """

    def get(self, request):
        """
        """

        return render(request, "acadamic_year.html")

class CreateAcademicsYear(View):
    """
    """

    def get(self, request):
        """
        """

        form = AcademicsForm()
        return render(request, 'new_year.html', {'form': form, 'heading': _('Add')})

    def post(self, request):
        """
        """

        form = AcademicsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            print "***************", name
            year_api.create_academics_year(name)
            return HttpResponseRedirect(reverse('academic_year'))
        else:
            messages.error(request, _('Please correct the errors below.'))
        return render(request, 'new_year.html', {'form': form, 'heading': _('Add')})

class AcademicYear(View):
    """
    """

    def get(self, request):
        """
        """
        page_no =  1#int(request.GET.get('start'))
        records_per_page = 10#int(request.GET.get('length'))
        page_no = page_no / records_per_page + 1

        years = year_api.get_all_years()
        data = []

        for index, year in enumerate(years.get('years', [])):
            year = [index+1,
            year.name,
            year.status,
            """<a href={0}> <span class='fa fa-pencil'>
            </span></a>""".format(reverse('update_year', kwargs={'year_id': year.id})),
            """<button class="btn btn-default delete_year mb-control" data-box="#mb-delete"id="{0}">
            <span class="fa fa-trash-o"></span></button>""".format(year.id)]
            data.append(year)
        print "data  ::: ", data

        response = {'recordsTotal': years.get('count'),
        'data': data, 'recordsFiltered': years.get('count')}

        return JsonResponse(response)

class UpdateYear(View):
    def post(self, request, year_id):
        form = AcademicsForm(request.POST)
        if form.is_valid():
            year_id = year_id
            year_name = form.cleaned_data.get('name','')
            year_api.update_year(year_id, year_name)#, year_status)
            return HttpResponseRedirect(reverse(acadamic_year))
        else:
            pass


class DeleteYear(View):
    def get(self, request, year_id):
        """
        """
        year_api.delete_year(year_id)
        messages.success(request, _('Year deleted successfully.'))
        return HttpResponseRedirect(reverse('acadamic_year'))